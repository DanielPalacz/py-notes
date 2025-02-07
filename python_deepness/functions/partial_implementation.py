from functools import update_wrapper

def partial_funct(func, *fixed_args, **fixed_kwargs):

    def wrapper(*args, **kwargs):
        return func(*fixed_args, *args, **fixed_kwargs, **kwargs)

    update_wrapper(wrapper, func)  # Copying metadata of original function (it will work on class methods nowa)
    return wrapper  # New function


def sum_this(a, b, c):
    return a + b + c


f = partial_funct(sum_this, 1, 2)


#

# partial implemented as Class:

class Partial:
    def __init__(self, func, *fixed_args, **fixed_kwargs):
        self.func = func
        self.fixed_args = fixed_args
        self.fixed_kwargs = fixed_kwargs

    def __call__(self, *args, **kwargs):
        return self.func(*self.fixed_args, *args, **self.fixed_kwargs, **kwargs)

# Tests:
sum_this2 = Partial(sum_this, 2)
print(sum_this2(8, 2))  # 12
