import time
from functools import cached_property
from timeit_decorator import print_timeit

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:

    def __getattribute__(self, attr_val, *kwargs):
        # print("[DeepThought][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
        return super().__getattribute__(attr_val)

    #@LazyProperty
    @cached_property
    def meaning_of_life(self):
        time.sleep(3)
        return 42

# my_deep_thought_instance = DeepThought()
#
# @print_timeit
# def wrapper(obj: DeepThought):
#     print(my_deep_thought_instance.meaning_of_life)
#
# wrapper(my_deep_thought_instance)
# wrapper(my_deep_thought_instance)
# wrapper(my_deep_thought_instance)
