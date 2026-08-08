
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Wejście")
    try:
        yield "101"
    finally:
        print("Wyjście")


with my_context() as something:
    print(something)
    print("Kod wewnątrz bloku")
