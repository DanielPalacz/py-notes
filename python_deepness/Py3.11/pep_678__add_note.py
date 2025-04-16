def process_file(filename):
    try:
        with open(filename) as f:
            data = f.read()
            raise ValueError("Coś poszło nie tak przy parsowaniu danych")
    except Exception as e:
        e.add_note(f"Podczas przetwarzania pliku: {filename}")
        raise

process_file(__file__)
