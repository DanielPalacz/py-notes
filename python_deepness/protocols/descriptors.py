


# Dynamic lookups


import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute



# Managed attributes - A popular use for descriptors is managing access to instance data

import logging

logging.basicConfig(level=logging.INFO)

class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)

class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1



#####################################################

# Custom validators

from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


#####################################################


# lazy_properties.py
import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:

    def __getattribute__(self, attr_val, *kwargs):
        print("[DeepThought][__getattribute__] Getting attribute '{}' value for {} as usual.".format(attr_val, self))
        return super().__getattribute__(attr_val)

    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42

# my_deep_thought_instance = DeepThought()
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)
# print(my_deep_thought_instance.meaning_of_life)

class AccessCounter:
    class DescriptorWrapper:
        """ Opakowanie wartości umożliwiające dostęp do metod deskryptora """
        def __init__(self, descriptor, instance):
            self.descriptor = descriptor
            self.instance = instance

        def __getattr__(self, attr):
            """ Jeśli pytamy o metodę deskryptora, przekazujemy ją dalej """
            if hasattr(self.descriptor, attr):
                return lambda *args, **kwargs: getattr(self.descriptor, attr)(self.instance, *args, **kwargs)
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")

        def __repr__(self):
            """ Zwraca reprezentację wartości bez zwiększania licznika """
            value = self.descriptor.data.get(self.instance, None)
            return repr(value)

        def __eq__(self, other):
            return self.get_value() == other

        def __bool__(self):
            """ Sprawdza, czy wartość jest ustawiona """
            return self.instance in self.descriptor.data

        def get_value(self):
            """ Zwraca przechowywaną wartość (zwiększa licznik odczytów) """
            if self.instance in self.descriptor.data:
                self.descriptor.read_count[self.instance] = (
                    self.descriptor.read_count.get(self.instance, 0) + 1
                )
                return self.descriptor.data[self.instance]
            return None

    def __init__(self):
        self.data = {}  # Przechowuje wartości dla różnych instancji
        self.read_count = {}  # Zlicza odczyty
        self.write_count = {}  # Zlicza zapisy
        self.wrapper_instances = {}  # Przechowuje wrappery dla instancji

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Obsługa dostępu z poziomu klasy

        # Jeśli wrapper już istnieje dla tej instancji, zwracamy ten sam obiekt
        if instance not in self.wrapper_instances:
            self.wrapper_instances[instance] = self.DescriptorWrapper(self, instance)

        return self.wrapper_instances[instance]

    def __set__(self, instance, value):
        # Blokujemy nadpisanie na poziomie klasy
        if isinstance(instance, type):
            raise AttributeError(f"Cannot overwrite descriptor on the class level.")

        self.write_count[instance] = self.write_count.get(instance, 0) + 1
        self.data[instance] = value

    def get_counts(self, instance):
        """Zwraca liczbę odczytów i zapisów dla konkretnej instancji"""
        return {
            "reads": self.read_count.get(instance, 0),
            "writes": self.write_count.get(instance, 0)
        }


class Test:
    counter = AccessCounter()


# Testujemy działanie
t = Test()

if t.counter:  # Sprawdza, czy wartość jest ustawiona
    print("Counter has a value")
else:
    print("Returning descriptor itself:", t.counter)  # Powinno zwrócić deskryptor

t.counter = 42  # Pierwszy zapis
print(t.counter.get_value())  # Odczyt wartości (teraz zwiększa licznik)
print(t.counter.get_value())  # Kolejny odczyt wartości

# Sprawdzamy licznik (Działa poprawnie!)
print(t.counter.get_counts())  # {'reads': 2, 'writes': 1}

# Kolejne odczyty
print(t.counter.get_value())
print(t.counter.get_counts())  # Licznik odczytów powinien być 3, a nie 5+
