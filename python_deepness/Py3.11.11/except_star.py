def raise_multiple_exceptions():
    raise ExceptionGroup(
        "Grupa wyjątków",
        [ValueError("Błąd wartości"), TypeError("Błąd typu")]
    )

try:
    raise_multiple_exceptions()
except* ValueError as e:
    print(f"Obsłużono ValueError: {e}")
except* TypeError as e:
    print(f"Obsłużono TypeError: {e}")
