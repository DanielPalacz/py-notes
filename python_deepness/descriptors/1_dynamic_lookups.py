import os


# Dynamic lookups


class DirectorySize:

    def __get__(self, obj, objtype=None):

        if obj is None:
            return self

        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute


# Edge case:
print("Edge Case, 'Directory.size':", Directory.size)
print()


d = Directory(".")
n = d.size
print(n)
