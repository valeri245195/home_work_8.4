from datetime import date, datetime


def get_birthdays_per_week(dict_users):

    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    today = date.today()

    if (today.year - 1) % 4 == 0:
        day_in_last_year = 366
    else:
        day_in_last_year = 365

    birthdays_per_week = {day: [] for day in days_of_week.values()}
    birthdays_per_week_empty = {day: [] for day in days_of_week.values()}
    ret_dict = {}
    counter = 0
    for user in dict_users:
        counter += 1
        birthday = user["birthday"]
        days_until_birthday = (birthday.replace(year=1) - today.replace(year=1)).days

        if birthday.month == today.month and birthday.day == today.day:
            continue  # Skip if it's today's birthday
        if today.month == 12 and birthday.month == 1:
            days_until_birthday += day_in_last_year
        if 0 <= days_until_birthday <= 6:
            day_of_week = days_of_week[(today.weekday() + days_until_birthday) % 7]
            birthdays_per_week[day_of_week].append(user["name"])

    if birthdays_per_week == birthdays_per_week_empty:
        return {}
    else:

        birthdays_per_week['Monday'] = birthdays_per_week['Saturday'] + birthdays_per_week['Monday']
        birthdays_per_week['Monday'] = birthdays_per_week['Sunday'] + birthdays_per_week['Monday']
        del birthdays_per_week['Sunday']
        del birthdays_per_week['Saturday']
        for key, value in birthdays_per_week.items():
            if birthdays_per_week[key] != birthdays_per_week_empty[key]:
                ret_dict.update({key: value})
    return ret_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
