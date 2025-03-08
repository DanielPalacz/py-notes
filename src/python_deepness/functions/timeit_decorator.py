import functools
from time import time_ns

def print_timeit(f):
    """ Decorator printing time of function execution """

    @functools.wraps(f)
    def function_wrapper(*args, **kwargs):
        t_start = time_ns()
        results = f(*args, **kwargs)
        t_end = time_ns()
        t = ( t_end - t_start ) / 1000000000
        t = t * 10 // 1 / 10
        print(f"Function {f.__name__} execution time: {t} s.")

        return results

    return function_wrapper
