import types

import inspect

def foo(x):
    y = x + 1
    print(inspect.currentframe())  # Current frame
    return y

foo(10)



def outer_func():
    name = "Pythonista"

    def inner_func():
        print(f"Hello, {name}!")

    return inner_func


funct = outer_func()

# Creating new cell/closure
closure_ = (types.CellType("Daniel"),)

# funct.__closure__ = new_closure
# AttributeError: readonly attribute

funct_hacked = types.FunctionType(funct.__code__, funct.__globals__, name=funct.__name__, closure=closure_)


# Achieving Encapsulation With Closures

def stack():
    _items = []

    def push(item):
        _items.append(item)

    def pop():
        return _items.pop()

    def closure():
        pass

    closure.push = push
    closure.pop = pop
    return closure
