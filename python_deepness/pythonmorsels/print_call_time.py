
from time import time
from functools import wraps


def print_call_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t1 = time()
        ret = f(*args, **kwargs)

        print(f.__name__, "call time:", time() - t1, "seconds")
        return ret

    return wrapper
