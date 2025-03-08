import functools

def decorate_funct(f):
    """ Decorator function: start_stop104 """

    @functools.wraps(f)
    def function_wrapper_level_one(*args, **kwargs):
        # Do something ...
        results = f(*args, **kwargs)
        # Do something ...
        return results

    return function_wrapper_level_one


@decorate_funct
def funct():
    return 100


# X = funct()
# print(X)


# Class related decorator

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("Number of calls:", self.num_calls)
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print("hello")


say_hello()
say_hello()
