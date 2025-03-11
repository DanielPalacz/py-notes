import time
from functools import cached_property


class InstanceCachedProperty:
    __slots__ = ('function_obj', 'function_name')

    def __init__(self, function):
        self.function_obj = function
        self.function_name = f"_{function.__name__}"


    def __get__(self, obj, objtype):
        if obj is None:
            return self

        if self.function_name not in obj.__dict__:
            obj.__dict__[self.function_name] = self.function_obj(obj)

        return obj.__dict__[self.function_name]

# cache współdzielony między instancjami jest rzadko stosowany w deskryptorach
# - lepiej trzymać cache jako atrybut klasy lub używać lru_cache zamiast kombinować z objtype.__dict__
class PerClassCache:
    __slots__ = ('function_obj', 'function_name')

    def __init__(self, function):
        self.function_obj = function
        self.function_name = f"_{function.__name__}"

    def __get__(self, obj, objtype):
        if obj is None:
            return self  # Dostęp przez klasę zwraca deskryptor

        # Cache w klasie
        if self.function_name not in objtype.__dict__:
            setattr(objtype, self.function_name, self.function_obj(obj))

        return getattr(objtype, self.function_name)


class DeepThought:

    # def __getattribute__(self, attr_val, *kwargs):
    #     # print("[DeepThought][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
    #     return super().__getattribute__(attr_val)

    # @PerClassCache
    # @InstanceCachedProperty
    @cached_property
    def meaning_of_life(self):
        time.sleep(3)
        return 42
