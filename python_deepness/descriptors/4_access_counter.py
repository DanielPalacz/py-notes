

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
# t = Test()
#
# if t.counter:  # Sprawdza, czy wartość jest ustawiona
#     print("Counter has a value")
# else:
#     print("Returning descriptor itself:", t.counter)  # Powinno zwrócić deskryptor

# t.counter = 42  # Pierwszy zapis
# print(t.counter.get_value())  # Odczyt wartości (teraz zwiększa licznik)
# print(t.counter.get_value())  # Kolejny odczyt wartości
#
# # Sprawdzamy licznik (Działa poprawnie!)
# print(t.counter.get_counts())  # {'reads': 2, 'writes': 1}
#
# # Kolejne odczyty
# print(t.counter.get_value())
# print(t.counter.get_counts())  # Licznik odczytów powinien być 3, a nie 5+
