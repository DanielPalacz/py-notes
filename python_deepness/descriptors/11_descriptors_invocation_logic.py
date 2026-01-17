import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

    # Adding below __set__ method results DirectorySize to be Data-Descriptor.
    #  - this changes invocation logic

    # def __set__(self, instance, value):
    #     raise AttributeError(f"{instance}, {value}")

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

d = Directory(".")
d.__dict__.update({"size": 31}) # it has effect only for Non-Data-Descriptors
print(d.size)
