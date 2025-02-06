# 1. Order of functions calls (descriptors)
#    - __getattribute__
#    - __get__
#    - not calling __getattr__

# 2. Order of functions calls (normal objects, not descriptors)
#    - __getattribute__
#    - not calling __get__ (because lack of as not descriptors)
#    - __getattr__


import os

class DirectorySize:    # Descriptor class

    def __get__(self, obj, objtype=None):
        print("[DirectorySize][__get__] Getting number of items in directory.")
        return len(os.listdir(obj.dirname))

class Directory:

    def __getattribute__(self, attr_val):
        print("[Directory][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
        return super().__getattribute__(attr_val)

    def __getattr__(self, attr_val):
      print("[Directory][__getattr__] Object '{}' does not have attribute '{}'. Not raising error as usual, returning None.".format(self, attr_val))
      return None
      # raise AttributeError(f"'Directory' object has no attribute '{attr_val}'")


    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

##################################################################################################################

d = Directory(".")
# size = d.size
name = d.name
# print(size)

# dirname_ = getattr(d, "dirname")
#
# try:
#     dirname_beta = getattr(d, "UnknownDir")
#     print(dirname_beta)
# except AttributeError:
#     pass
#

# f = getattr
#
# def getattr(obj, attr_val):
#     print("Running getattr builtin function.")
#     f(d, "size")
#
# getattr(d, "size")
# size = d.size


class PersonSurname:    # Descriptor class

    def __get__(self, obj, objtype=None):
        print("[PersonSurname][__get__] Returning a Person surname.")
        return "Surname Unknown"


class Person:

    surname = PersonSurname()

    def __init__(self, name):
        self._name = name          # Regular instance attribute

    def __getattribute__(self, attr_val):
        print("[Person][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
        return super().__getattribute__(attr_val)

    def __getattr__(self, attr_val):
      print("[Person][__getattr__] Object '{}' does not have attribute '{}'. Not raising error as usual, returning None.".format(self, attr_val))
      return None
      # raise AttributeError(f"'Directory' object has no attribute '{attr_val}'")

