

# def is_iterator_object(obj):
#     return hasattr(obj, "__iter__") and hasattr(obj, "__next__")

# nie sprawdza, czy __iter__ zwraca self, ignoruje rejestrację w ABC (collections.abc.Iterator)
# łatwo złapać false-positive (ktoś może mieć metody, ale nie zachowywać się jak iterator)
# dobra dydaktycznie: pokazuje z czego składa się iterator, ale w praktyce ABC wygrywa


class InfCounter:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 10000000000000000000000:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Iterable Edge Case:
class CustomSeq:
    def __getitem__(self, index):
        if index >= 5:
            raise IndexError
        return index * 2


from collections.abc import Iterable, Iterator, Sequence


def is_iterator_object(obj: object) -> bool:
    return isinstance(obj, Iterator)


def is_iterable_object(obj: object) -> bool:
    return isinstance(obj, Iterable)


def is_sequence_object(obj: object) -> bool:
    return isinstance(obj, Sequence)
