
# What is the design thinking behind `@property`?
#
# Primary design pressures:
# - Avoiding update anomalies and invalid object state
# - Managing mutability without overexposing internals
# - Preserving encapsulation while minimizing boilerplate
#
# Premises:
# - Library authors should avoid up-front implementation decisions that force
#   user-side code churn over time.
#   Churn includes rewrites, refactors, breaking changes, or repeated adjustments
#   in downstream code.
# - Mutability is inherently risky when access to state is uncontrolled, as it can
#   introduce update anomalies and violate invariants.
#
# Key considerations for library design:
# - The ratio of library code to user code:
#   A single line of library code can eliminate many lines of user code, magnifying
#   design decisions.
# - Discoverability and fan-out:
#   Attributes referenced in many places are costly to change later.
#   Attributes are highly discoverable and widely referenced; changing them later is expensive.
#   @property mitigates this by freezing the access syntax early.
# - Where invariants are enforced:
#   Should update anomalies be prevented on write, on read, or both?
# - “Const-ness” and read-only attributes:
#   These are largely matters of convention unless enforced by the API.
#
# Conclusion:
# - Library authors need an intermediate form of access to object state—one that
#   presents a stable, attribute-like interface to users while retaining the
#   freedom to evolve validation, computation, and storage strategies internally.
# - `@property` provides this intermediate abstraction by decoupling interface
#   from implementation without imposing early rigidity.
# #



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
