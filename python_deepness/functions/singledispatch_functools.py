from functools import singledispatch

# Generic paradigm:
#  - singledispatch to świetne narzędzie do funkcji generycznych w Pythonie
#  - singledispatchmethod (wersja do metod klasowych od Pythona 3.8)


# Definiujemy funkcję generyczną
@singledispatch
def process(value):
    """Domyślna implementacja"""
    print(f"Nie wiem jak obsłużyć: {value!r}")

# Rejestrujemy wariant dla int
@process.register(int)
def _(value):
    print(f"Liczba całkowita: {value}, podwojona: {value * 2}")

# Rejestrujemy wariant dla str
@process.register(str)
def _(value):
    print(f"Napis: {value.upper()}")

# Rejestrujemy wariant dla list
@process.register(list)
def _(value):
    print(f"Lista z {len(value)} elementami: {value}")

# ---- Użycie ----
process(42)          # -> Liczba całkowita: 42, podwojona: 84
process("python")    # -> Napis: PYTHON
process([1, 2, 3])   # -> Lista z 3 elementami: [1, 2, 3]
process(3.14)        # -> Nie wiem jak obsłużyć: 3.14
