import os


# Dynamic lookups


class DirectorySize:

    def __get__(self, obj, objtype=None):

        if obj is None:
            return self

        print(locals())

        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute


# Edge case:
Directory.size

d = Directory(".")
n = d.size
print(n)
