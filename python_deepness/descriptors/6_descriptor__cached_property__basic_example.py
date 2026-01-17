import time
# from functools import cached_property

# Default Cache Property - not shared between instances:

# class LazyProperty:
#     def __init__(self, function):
#         self.function = function
#         self.name = function.__name__
#
#     def __get__(self, obj, objtype=None) -> object:
#         obj.__dict__[self.name] = self.function(obj)
#         return obj.__dict__[self.name]


class InstanceCachedProperty:
    __slots__ = ('function_obj', 'function_name')

    def __init__(self, function):
        self.function_obj = function
        self.function_name = None  # Set later, by __set_name__

    def __set_name__(self, owner, name):
        self.function_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.function_name not in obj.__dict__:
            obj.__dict__[self.function_name] = self.function_obj(obj)

        return obj.__dict__[self.function_name]

# Cache Property - shared between instances:
#  - it is rarely seen solution in Descriptors
#  - better stores Cache as Class attribute (or use lru_cache) instead of combinations with Class.__dict__

# class PerClassCache:
#     __slots__ = ('function_obj', 'function_name')
#
#     def __init__(self, function):
#         self.function_obj = function
#         self.function_name = f"_{function.__name__}"
#
#     def __get__(self, obj, objtype):
#         if obj is None:
#             return self                             # Access from class level
#
#         # Cache inside class object
#         if self.function_name not in objtype.__dict__:
#             setattr(objtype, self.function_name, self.function_obj(obj))
#
#         return getattr(objtype, self.function_name)


class DeepThought:
    # def __getattribute__(self, attr_val, *kwargs):
    #     # print("[DeepThought][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
    #     return super().__getattribute__(attr_val)

    @InstanceCachedProperty
    #@cached_property
    def meaning_of_life(self):
        time.sleep(3)
        return 42
