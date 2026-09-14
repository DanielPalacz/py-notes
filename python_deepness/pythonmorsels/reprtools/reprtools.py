def format_arguments(*args, **kwargs) -> str:
    output = ", ".join([repr(a) for a in args])

    if kwargs and args:
        for k, v in kwargs.items():
            output += f", {k}={v!r}"

    elif kwargs and not args:
        temp_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        output = ", ".join(temp_list)

    return output


def make_repr(*args, **kwargs):
    """Make a repr method for the class."""

    def repr(self):
        args_names = kwargs.get("args", [])
        kwargs_names = kwargs.get("kwargs", [])

        args_values = [
            self.__dict__[name]
            for name in args_names
        ]

        kwargs_values = {
            name: self.__dict__[name]
            for name in kwargs_names
        }

        args_string = format_arguments(
            *args_values,
            **kwargs_values,
        )

        return f"{type(self).__name__}({args_string})"

    return repr
