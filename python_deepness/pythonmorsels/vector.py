class Vector:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)
        object.__setattr__(self, "z", z)

    def __setattr__(self, name, value):
        raise AttributeError("Vectors are immutable.")

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.z == other.z
        )

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        try:
            return Vector(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z,
            )
        except AttributeError:
            raise TypeError("AttributeError initially raised.")

    def __sub__(self, other):
        try:
            return Vector(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
            )
        except AttributeError:
            raise TypeError("AttributeError initially raised.")

    def __mul__(self, other_scalar):

        if not isinstance(other_scalar, int):
            raise TypeError("Incorrect scalar type.")

        return Vector(
            self.x * other_scalar,
            self.y * other_scalar,
            self.z * other_scalar
        )

    def __rmul__(self, other_scalar):

        if not isinstance(other_scalar, int):
            raise TypeError("Incorrect scalar type.")

        return Vector(
            self.x * other_scalar,
            self.y * other_scalar,
            self.z * other_scalar
        )

    def __truediv__(self, other_scalar):

        if not isinstance(other_scalar, int):
            raise TypeError("Incorrect scalar type.")

        return Vector(
            self.x / other_scalar,
            self.y / other_scalar,
            self.z / other_scalar
        )
