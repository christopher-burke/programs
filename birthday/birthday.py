#!/usr/bin/env python3

"""Birthday countdown program."""

from datetime import date as dt


def get_users_birthday() -> dt:
    """Get the user's birthday.

    YYYY MM DD format is expected.
    Returns a datetime.date object of the date.
    """
    year, month, day = map(int, input(
        'Enter your birthday [YYYY MM DD]: ').split(' '))
    return dt(year, month, day)


def compute_diff(start_date: dt, end_date: dt):
    """Calculate the difference betweeen start date and end date.

    Retruns int - difference between dates.
    """
    this_year = dt(end_date.year,
                   start_date.month,
                   start_date.day,
                   )

    diff = this_year - end_date
    return diff.days


def birthday_day_info(num_days: int):
    """Print the information to the user about the birtdate entered.

    if birthday is in the past -> Print # of day(s) since birthday.
    if birthday is in the future -> Print # of day(s) until birthday
    if today is birthday -> State today is your birthday
    and say happy birthday.

    """
    plural = "s" if abs(num_days) > 1 else ''
    if num_days < 0:
        print(f'Your birthday {abs(num_days)} day{plural} ago.')
    elif num_days > 0:
        print(f'Your birthday is in {abs(num_days)} day{plural}.')
    else:
        print('Today is your Birthday! Happy Birthday!')


def main():
    """Main function of birthday program."""
    bday = get_users_birthday()
    now = dt.today()
    num_days = compute_diff(bday, now)
    birthday_day_info(num_days)


if __name__ == "__main__":
    main()
