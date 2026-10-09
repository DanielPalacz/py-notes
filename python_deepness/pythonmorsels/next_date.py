from datetime import date
from datetime import timedelta


class NextDate:
    def __init__(self, next_day: int):
        self.next_day = next_day

    def __str__(self):
        name_day = Weekday.get_name(self.next_day)
        return f"NextDate(Weekday.{name_day})"

    def __repr__(self):
        name_day = Weekday.get_name(self.next_day)
        return f"NextDate(Weekday.{name_day})"

    def date(self):
        today = date.today()
        days = (self.next_day - today.weekday()) % 7
        return today + timedelta(days=days)

    def days_until(self):
        today = date.today()
        return (self.next_day - today.weekday()) % 7


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @classmethod
    def get_name(cls, num_day):
        for name, value in cls.__dict__.items():
            if value == num_day:
                return name

        return "MONDAY"
