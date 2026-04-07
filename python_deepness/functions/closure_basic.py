
def f():

    x = 1
    y = 2
    z = 3

    def gx():
        return x + y + z + 1

    return gx


g = f()
X = [cl.cell_contents for cl in g.__closure__]
print(X)


# W kontekście domknięć (closures), co się dzieje ze zmiennymi z zakresu Enclosing po zakończeniu działania funkcji zewnętrznej?
#  -- Są zapamiętywane w atrybucie __closure__ funkcji wewnętrznej.
