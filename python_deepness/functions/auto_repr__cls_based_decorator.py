
def auto_repr(args=None, kwargs=None):
    """Class decorator to automatically create a __repr__."""
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}

    def wrapper(cls):
        cls.__repr__ = make_repr(args, kwargs)
        return cls

    return wrapper


def format_arguments(args, kwargs):
    arg_strings = (
        repr(a)
        for a in args
    )
    kwarg_strings = (
        f"{name}={value!r}"
        for name, value in kwargs.items()
    )
    return ", ".join([*arg_strings, *kwarg_strings])


def make_repr(args=(), kwargs=()):
    """Make a repr method for the class."""
    def __repr__(self):
        arg_values = [self.__dict__[a] for a in args]
        kwarg_values = {a: self.__dict__[a] for a in kwargs}
        arg_string = format_arguments(arg_values, kwarg_values)
        return f"{type(self).__name__}({arg_string})"
    return __repr__

