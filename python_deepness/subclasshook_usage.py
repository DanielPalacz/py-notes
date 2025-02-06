from abc import ABCMeta, abstractmethod


class FileLike(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is FileLike:
            if any("read" in B.__dict__ and "write" in B.__dict__ for B in subclass.__mro__):
                return True  # uznajemy za podklasę!
        return NotImplemented  # sprawdzaj normalne dziedziczenie


# Klasa nie dziedziczy z FileLike, ale spełnia warunki
class CustomFile:
    def read(self):
        return "Reading data"

    def write(self, data):
        print(f"Writing {data}")


# Normalnie issubclass() zwróciłoby False, ale dzięki __subclasshook__:
print(issubclass(CustomFile, FileLike))  # True!
