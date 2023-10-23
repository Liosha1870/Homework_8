from datetime import datetime, timedelta, date, time

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    if not users:
        return {}

    today = date.today()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays_per_week = {day: [] for day in days_of_week}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        current_day_of_week = today.weekday()
        birthday_day_of_week = days_of_week[(current_day_of_week + days_until_birthday) % 7]

        if days_until_birthday > 0 and days_until_birthday <= 7:
            if birthday_day_of_week in ["Saturday", "Sunday"]:
                next_week_day = "Monday"
                birthdays_per_week[next_week_day].append(name)
            else:
                birthdays_per_week[birthday_day_of_week].append(name)

    birthdays_per_week = {day: users for day, users in birthdays_per_week.items() if users}

    return birthdays_per_week
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
