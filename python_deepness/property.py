

class A:
    def __init__(self):
        self._y = None

    def x(self):
        return self._y

    def z(self, value):
        self._y = value

    y = property(fget=x, fset=z)


class B:

    def __init__(self):
        self._y = None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
