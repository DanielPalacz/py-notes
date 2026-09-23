import datetime
from typing import Optional
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def _get_first_weekday_of_the_month(year: int, month: int, weekday: int) -> Optional[int]:
    for day in range(1, 8):

        day_datetime = datetime.date(year, month, day)
        if day_datetime.weekday() == weekday:
            return day

    return None


def _get_last_weekday_of_the_month(year: int, month: int, weekday: int) -> Optional[int]:
    for day in range(31, 21, -1):

        try:
            day_datetime = datetime.date(year, month, day)
            if day_datetime.weekday() == weekday:
                return day
        except ValueError:
            pass

    return None


def meetup_date(year: int, month: int, nth: int = 4, weekday: int = Weekday.THURSDAY) -> datetime.date:
    # if isinstance(weekday, Weekday):
    #     weekday = weekday.value

    d1 = datetime.date(year, month, 1)

    if nth < 0:
        day = _get_last_weekday_of_the_month(year, month, weekday)
        meetup_day_int = day + (nth * 7 + 7)

    else:
        day = _get_first_weekday_of_the_month(year, month, weekday)
        meetup_day_int = day + (nth * 7 - 7)

    return datetime.date(year, month, meetup_day_int)
