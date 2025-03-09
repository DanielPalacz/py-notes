class MethodType:
    "Emulate PyMethod_Type in Objects/classobject.c"

    def __init__(self, func, obj):
        self.__func__ = func
        self.__self__ = obj

    def __call__(self, *args, **kwargs):
        func = self.__func__
        obj = self.__self__
        print("[MethodType] Running __call__.")
        return func(obj, *args, **kwargs)

    def __getattribute__(self, name):
        "Emulate method_getset() in Objects/classobject.c"
        if name == '__doc__':
            return self.__func__.__doc__
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        "Emulate method_getattro() in Objects/classobject.c"
        return getattr(self.__func__, name)

    def __get__(self, obj, objtype=None):
        "Emulate method_descr_get() in Objects/classobject.c"
        print("[MethodType] Running __get__.")
        return self

class FunctionFakeSubstitute:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, objtype=None):
        if obj is None:
            print(f"[FunctionFake] Returning {type(self)} object.")
            return self

        print("[FunctionFake] Returning MethodType object.")
        return MethodType(self.func, obj)

class A:
    @FunctionFakeSubstitute
    def foo(self):
        print("Original foo() called.")

    def bar(self):
        print("Original bar() called.")


@FunctionFakeSubstitute
def funct1():
    print("Original funct() called.")


def funct2():
    print("Original funct() called.")


class X:
    def f(self):
        pass

    @classmethod
    def g(cls):
        pass


print(X().f)
print(X().g)
