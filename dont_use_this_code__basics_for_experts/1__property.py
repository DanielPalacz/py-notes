
# What is the design thinking behind `@property`?
#  - update anomalies, mutability, privateness
#  - style of avoiding boilerplate

    # Premises:
    #  - we want to avoid up-front decision-making that could cause User-side code "churn"
    #    Churn: Ongoing rewrites, refactors, breaking changes, or adjustments that users must make over time.
    #  - mutability introduces risks (risks of: update anomalies or invalid data)

    # Consider:
    #  * the ratio of lines of Library-code vs User-code (one line of code eliminates 10 lines o User code)
    #  * discoverability of User-code (used in many places? fan-out effect)
    #  * do we address update anomaly on read or on write?
    #  * const-ness, read-only attributes are matter of convention and guidance


# Conclusion: "We need intermediate access to object state." -> @property



from dataclasses import dataclass


@dataclass
class T1:
    _x: int
    y: int

    def __post_init__(self):
        self.x = self._x


    @property
    def x(self):
        return self._x

    @x.setter # validation is on write
    def x(self, value):
        if value < 0:
            raise ValueError("x must be positive")
        self._x = value


class T2:

    def __init__(self, x, y):
        self.x = x
        self._y = None

    @property # validation is on read
    def x(self):
        if self._x < 0:
            raise ValueError("x must be positive")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    y = property(lambda self: self._y)

    @y.setter
    def y(self, value):
        self._y = value


# from collections import namedtuple # immutable
#
# T3 = namedtuple('T3', ['x', 'y'])
# t3_obj = T3(1, 2)
