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

    d1 = datetime.date(year, month, 1)

    if nth < 0:
        day = _get_last_weekday_of_the_month(year, month, weekday)
        meetup_day_int = day + (nth * 7 + 7)

    else:
        day = _get_first_weekday_of_the_month(year, month, weekday)
        meetup_day_int = day + (nth * 7 - 7)

    return datetime.date(year, month, meetup_day_int)


# meetup_date(2016, 2, -1)
# meetup_date(2018, 1, nth=-2, weekday=0)

import datetime
import unittest

# from meetup_date import meetup_date


class MeetupDateTests(unittest.TestCase):

    """Tests for meetup_date."""

    def test_aug_2015(self):
        self.assertEqual(meetup_date(2015, 8), datetime.date(2015, 8, 27))

    def test_sept_2015(self):
        self.assertEqual(meetup_date(2015, 9), datetime.date(2015, 9, 24))

    def test_oct_2015(self):
        self.assertEqual(meetup_date(2015, 10), datetime.date(2015, 10, 22))

    def test_jan_2016(self):
        self.assertEqual(meetup_date(2016, 1), datetime.date(2016, 1, 28))

    def test_feb_2016(self):
        self.assertEqual(meetup_date(2016, 2), datetime.date(2016, 2, 25))

    # Bonus 1
    # @unittest.expectedFailure
    def test_allow_week_and_weekday_to_be_specified(self):
        # Fourth Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=4, weekday=3),
            datetime.date(2016, 2, 25),
        )
        # First Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=1, weekday=0),
            datetime.date(2018, 1, 1),
        )
        # Fourth Saturday
        self.assertEqual(
            meetup_date(2018, 1, nth=4, weekday=5),
            datetime.date(2018, 1, 27),
        )
        # Fifth Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=5, weekday=2),
            datetime.date(2018, 1, 31),
        )
        # Second Tuesday
        self.assertEqual(
            meetup_date(2018, 2, nth=2, weekday=1),
            datetime.date(2018, 2, 13),
        )

    # Bonus 2
    # @unittest.expectedFailure
    def test_allow_specifying_from_end_of_month(self):
        # Last Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=-1, weekday=3),
            datetime.date(2016, 2, 25),
        )
        # Last Friday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=4),
            datetime.date(2018, 1, 26),
        )
        # Last Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=2),
            datetime.date(2018, 1, 31),
        )
        # Last Saturday
        self.assertEqual(
            meetup_date(2018, 3, nth=-1, weekday=5),
            datetime.date(2018, 3, 31),
        )
        # Second to last Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=-2, weekday=0),
            datetime.date(2018, 1, 22),
        )

    # Bonus 3
    # @unittest.expectedFailure
    def test_add_Weekday_object(self):
        from meetup_date import Weekday
        # First Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=1, weekday=Weekday.MONDAY),
            datetime.date(2018, 1, 1),
        )
        # Second Tuesday
        self.assertEqual(
            meetup_date(2018, 2, nth=2, weekday=Weekday.TUESDAY),
            datetime.date(2018, 2, 13),
        )
        # Fifth Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=5, weekday=Weekday.WEDNESDAY),
            datetime.date(2018, 1, 31),
        )
        # Fourth Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=4, weekday=Weekday.THURSDAY),
            datetime.date(2016, 2, 25),
        )
        # Last Friday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=Weekday.FRIDAY),
            datetime.date(2018, 1, 26),
        )
        # Last Saturday
        self.assertEqual(
            meetup_date(2018, 6, nth=-1, weekday=Weekday.SATURDAY),
            datetime.date(2018, 6, 30),
        )
        # Fourth Sunday
        self.assertEqual(
            meetup_date(2018, 6, nth=4, weekday=Weekday.SUNDAY),
            datetime.date(2018, 6, 24),
        )
        self.assertEqual(Weekday.MONDAY, 0)
        self.assertEqual(Weekday.TUESDAY, 1)
        self.assertEqual(Weekday.WEDNESDAY, 2)
        self.assertEqual(Weekday.THURSDAY, 3)
        self.assertEqual(Weekday.FRIDAY, 4)
        self.assertEqual(Weekday.SATURDAY, 5)
        self.assertEqual(Weekday.SUNDAY, 6)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
