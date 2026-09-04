
from functools import wraps

def only_once(f):
    f.was_run = False

    @wraps(f)
    def wrapper(*args, **kwargs):
        if f.was_run:
            raise ValueError("You can't call this function twice!")

        results = f(*args, **kwargs)
        f.was_run = True
        return results

    return wrapper
