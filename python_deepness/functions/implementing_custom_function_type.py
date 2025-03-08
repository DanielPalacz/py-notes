import inspect
import pickle

class CustomFunctionType:
    def __init__(self, name, argnames, defaults=(), code_str="", filename="my_script.py", lineno=1):
        self.__name__ = name
        self.__qualname__ = name
        self.__defaults__ = defaults if defaults else ()
        self.__kwdefaults__ = None
        self.__annotations__ = {}
        self.__doc__ = None
        self.__globals__ = globals()

        # Przechowujemy kod źródłowy
        self.code_str = code_str
        compiled_code = compile(code_str, filename, "exec")
        self.__locals__ = {}
        exec(compiled_code, self.__globals__, self.__locals__)  # Uruchamiamy kod
        self.func = self.__locals__[name]  # Pobieramy funkcję

        # Tworzymy __signature__ dla introspekcji
        params = [inspect.Parameter(arg, inspect.Parameter.POSITIONAL_OR_KEYWORD) for arg in argnames]
        self.__signature__ = inspect.Signature(params)

        # Przechowujemy kod, aby umożliwić pickle
        self.__code__ = compiled_code.co_consts[0]

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)  # Wywołujemy funkcję

    def __repr__(self):
        return f"<MyFunction {self.__name__} at {hex(id(self))}>"

    def __get__(self, instance, owner):
        """Obsługuje przypadek wywołania jako metoda instancji"""
        if instance is None:
            return self
        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)  # Wiąże self do instancji

    def __reduce__(self):
        """Obsługa pickle"""
        return (self.__class__, (self.__name__, self.__code__.co_varnames, self.__defaults__, self.code_str))

    def __signature__(self):
        """Obsługuje inspect.signature()"""
        return self.__signature__

    def getsource(self):
        """Zwraca kod źródłowy funkcji"""
        return self.code_str

    @staticmethod
    def _recreate_from_code_str(name, argnames, defaults, code_str):
        """Metoda statyczna do odtworzenia funkcji z kodu"""
        return CustomFunctionType(name, argnames, defaults, code_str)

# ==== TESTY ====

# ✅ Test: Działa jak zwykła funkcja
print("✅ Test: Normalna funkcja")
my_func = CustomFunctionType("double", ("x",), (), """
def double(x):
    return x * 2
""")
print(my_func(5))  # 10

# ✅ Test: introspekcja działa
print("\n✅ Test: inspect.signature()")
print(inspect.signature(my_func))  # (x,)

# ✅ Test: Pickle działa
print("\n✅ Test: Pickle")
serialized = pickle.dumps(my_func)
deserialized = pickle.loads(serialized)
print(deserialized(5))  # 10

# ✅ Test: Działa z dekoratorami
print("\n✅ Test: Dekoratory")
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

wrapped = decorator(my_func)
print(wrapped(5))  # Powinno wydrukować nazwę i wynik

# ✅ Test: Działa z introspekcją
print("\n✅ Test: inspect.signature()")
print(inspect.signature(my_func))  # (x,)

# ✅ Test: Działa z `map()`, `sorted()`, `filter()`
print("\n✅ Test: map(), sorted(), filter()")
print(list(map(my_func, [1, 2, 3])))  # [2, 4, 6]
print(sorted([3, 1, 2], key=my_func))  # [1, 2, 3]

# ✅ Test: Działa z pickle
print("\n✅ Test: Pickle")
serialized = pickle.dumps(my_func)
deserialized = pickle.loads(serialized)
print(deserialized(5))  # 10

# ✅ Test: Działa z inspect.getsource()
print("\n✅ Test: inspect.getsource() [it is not implemented, [TypeError]]")
#
# try:
#     print(inspect.getsource(my_func))
# except TypeError:
#     print(my_func.code_str)
print("----------------------------------------------------------------------------------------------")

# Goal was to have implementation of CustomFunctionType that is not based on types.FunctionType
# - we want to simulate function behaviour from scratch without builtin FunctionType

# It means that we need to
#  - execute function code in __call__() - not delegate this
#  - implement local variables and argument management
#  - implement logic for closures
#  - allow introspection (fe. inspect.signature())
#  - handle class methods correctly
#  - implement serialization logic (pickle)
#  - check across different Python Use cases
print("----------------------------------------------------------------------------------------------")

new_funct = CustomFunctionType("triple", ("x",), (), """
def triple(x):
    return x * 3
""")
print(new_funct(5))  # 15
