class Immutable:

    __slots__ = ('_dept', '_name')          # Replace the instance dictionary

    def __init__(self, dept, name):
        self._dept = dept                   # Store to private attribute
        self._name = name                   # Store to private attribute

    @property                               # Read-only descriptor
    def dept(self):
        return self._dept

    @property
    def name(self):                         # Read-only descriptor
        return self._name


def immutable_class(**kwargs):
    class ImmutableMeta(type):

        # Metoda __call__ w metaklasie kontroluje tworzenie instancji:
        def __call__(cls, *args, **kwargs):
            raise TypeError(f"Immutable class doesn't support instances creation. [Class: {cls.__name__}, args: {args}, kwargs: {kwargs}].")

        # Użycie __getattr__:
        # - dla klas dostęp do atrybutów jest domyślnie obsługiwany przez __getattribute__ (wywołyje __getattr__)
        # - nadpisanie wyjątku to __getattr__ w metaklasie jest ok (tylko obsługa nieistniejących atrybutów)
        def __getattr__(cls, name):
            raise AttributeError(f"Immutable class doesn't have that attribute [Class: {cls.__name__}, attribute: {name}].")

        def __setattr__(cls, name, value):
            raise AttributeError(f"Immutable class attribute can't be added or overridden [Class: {cls.__name__}, attribute: {name}].")


    # def _no_instances(self, *args, **kwargs_):
    #     raise AttributeError(f"Immutable class doesn't support instances creation. [Class: {self.__name__}, args: {args}, kwargs: {kwargs_}].")

    # def _setattr(cls, name, value):
    #     raise AttributeError(f"Immutable class attribute can't be added or override [Class: {cls.__name__}, attribute: {name}].")
    #
    # To ok, ale -> call
    #   _cls.__init__ = _no_instances
    #   _cls.__new__ = _no_instances
    # _cls.__setattr__ = _setattr  # To nie działało, bo __setattr__ operuje na instancjach

    # _all = {k: v for k, v in ImmutableMeta("ImmutableCls", (), kwargs).__dict__.items() if not k.startswith("__")}
    # _kwargs = {k: v for k, v in kwargs.items()}
    # kwargs.update({"ALL": _kwargs})
    # _cls = ImmutableMeta("ImmutableCls", (), dict(**kwargs, **{"ALL": _kwargs}))
    # return ImmutableMeta("ImmutableCls", (), kwargs)

    _cls = ImmutableMeta("ImmutableCls", (), kwargs | {"ALL": kwargs.copy()})
    return _cls



C = immutable_class(A=1, B=2, C=3, D=4)

CONSTANTS = {
    "INCH": 2.54,
    "PI": 3.14,
    "ELLIPSIS": ...
}

CONSTANTS_CLS = immutable_class(**CONSTANTS)
# breakpoint()