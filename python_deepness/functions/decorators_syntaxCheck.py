
from functools import wraps

def decorator(f):
    print("[Decorator] - external body execution.]")

    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@decorator
def foo() -> int:
    print("It is fun.")
    return 11

foo_out = foo()
