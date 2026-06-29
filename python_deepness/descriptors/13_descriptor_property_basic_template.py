
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
            )
        setattr(obj, self.private_name, value)
