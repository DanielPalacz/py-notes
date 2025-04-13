def licznik():
    total = 0
    while True:
        x = yield
        if x is None:
            break
        total += x
    return total  # to zostanie zwrócone jako StopIteration.value

def deleguj():
    wynik = yield from licznik()  # delegacja z odbiorem wartości końcowej
    print(f"Suma: {wynik}")


# gen = deleguj()
# next(gen)           # uruchamiamy generator (aż do pierwszego yield)
# gen.send(10)
# gen.send(20)
# gen.send(5)
# gen.send(None)      # kończymy — licznik zwróci total, yield from go odbierze
