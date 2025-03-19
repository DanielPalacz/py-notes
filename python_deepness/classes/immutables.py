import time
from functools import cached_property


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

        # Metoda __call__ jeśli jest zaimplementowana w metaklasie to kontroluje tworzenie instancji
        def __call__(cls, *args, **kwargs):
            print("Checking....")
            raise TypeError(f"Immutable class doesn't support instances creation. [Class: {cls.__name__}, args: {args}, kwargs: {kwargs}].")

        # Użycie __getattr__:
        # - dostęp do atrybutów jest obsługiwany przez __getattribute__ (wywołyje __getattr__)
        #   ---> różne implementacje: type, object, super
        def __getattr__(cls, name):
            raise AttributeError(f"Immutable class doesn't have that attribute [Class: {cls.__name__}, attribute: {name}].")

        def __setattr__(cls, name, value):
            raise AttributeError(f"It is immutable class. Attribute adding or overriding is prohibited [Class: {cls.__name__}, attribute: {name}, value: {value}].")

    _cls = ImmutableMeta("ImmutableCls", (), kwargs | {"ALL": kwargs.copy()})
    return _cls



C = immutable_class(A=1, B=2, C=3, D=4)

CONSTANTS = {
    "INCH": 2.54,
    "PI": 3.14,
    "ELLIPSIS": ...
}

CONSTANTS_CLS = immutable_class(**CONSTANTS)
