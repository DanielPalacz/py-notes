

from functools import wraps
from time import perf_counter


def print_call_info(function=None, *, time=True):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            ret_val = func(*args, **kwargs)
            runtime = perf_counter() - start

            call = f"{func.__name__}({format_args(args, kwargs)})"

            if time:
                print(f"{call} returned {ret_val} ({runtime} seconds)")
            else:
                print(f"{call} returned {ret_val}")

            return ret_val

        return wrapper

    # @print_call_info
    if function is not None:
        return actual_decorator(function)

    # @print_call_info(...)
    return actual_decorator


def format_args(args, kwargs):
    arg_strings = (
        repr(a)
        for a in args
    )
    kwarg_strings = (
        f"{name}={value!r}"
        for name, value in kwargs.items()
    )
    return ", ".join([*arg_strings, *kwarg_strings])
