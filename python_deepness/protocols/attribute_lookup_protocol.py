import os

class DirectorySize:    # Descriptor class

    def __get__(self, obj, objtype=None):
        print("[DirectorySize][__get__] Getting number of items in directory.")
        return len(os.listdir(obj.dirname))

class Directory:

    def __getattribute__(self, attr_name):
        print("[Directory][__getattribute__] Getting attribute '{}' for {} object as usual.".format(attr_name, self))
        return super().__getattribute__(attr_name)
    # return object.__getattribute__(self, attr_name)

    def __getattr__(self, attr_name):
      print("[Directory][__getattr__] Object '{}' does not have attribute '{}'. Not raising AttributeError as usual, returning 'No attribute' string.".format(self, attr_name))
      # return "No attribute " + "'" + attr_name + "'"
      raise AttributeError(f"'Directory' object has no attribute {attr_name}")


    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute


d = Directory(".")
d.existing = 123

print("directory name:", d.dirname)
print()
print(d.existing)
print()
print(d.missing)
print()
