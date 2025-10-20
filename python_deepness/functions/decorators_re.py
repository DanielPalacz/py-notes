

def decorator(f):
    return f
                ## @decorator kompiluje się do:
                ## foo = decorator(foo)
                    ## i w runtime to:
                    ## PyObject_Call(decorator, args, kwargs)
                    ##  - ponieważ decorator jest typu function, to:
                    ##  - jego tp_call jest bezpośrednio wywoływane a nie szuka __call__

decorator.__call__ = lambda f: print("HA!")

@decorator
def foo():
    pass
#            # To i tak nie wywoła decorator.__call__
#             # decorator(foo) wywoła po prostu tp_call — bez zaglądania w __call__
#             #  - function to typ wbudowany (C-level PyFunction_Type) i __call__ nie jest jej mechanizmem wywoływania
#             #  - tylko obiekty z __call__ (np. instancje klas, które mają __call__) są wywoływane poprzez __call__
#
#                 # LOAD_GLOBAL 0 (decorator)
#                 # LOAD_CONST <code object funct>
#                 # MAKE_FUNCTION
#                 # CALL_FUNCTION 1



foo()


import sys


# DEKORATORY KLASOWE

class CountCalls:
    print("[CountCalls] Class creation flow.")

    def __init__(self, f):
        print("[Dekorator syntax][CountCalls] __init__")
        self.func = f
        self.num_calls = 0

    def __new__(cls, f):
        print("[Dekorator syntax][CountCalls] __new__")
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("[Dekorator call][CountCalls] __call__ [", "args: ", args, ", kwargs: ", kwargs, ", num_calls: ", self.num_calls, "]", sep="")
        return self.func(*args, **kwargs)

# [CountCalls] Class creation flow


@CountCalls
def funct(text):
    print(text)

# [Dekorator syntax][CountCalls] __new__
# [Dekorator syntax][CountCalls] __init__

funct("Now.")
funct("Now.")
# [Dekorator call][CountCalls] __call__ [args: ('Now.',), kwargs: {}]
# Now.



