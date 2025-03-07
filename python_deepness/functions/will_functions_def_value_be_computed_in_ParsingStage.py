import dis

def example():
    x = 42
    print(x)

# print(dis.dis(example))  # Pokazuje skompilowany bajtkod


def def_value():
    print("def_value executed")
    return 42

print("Checkpoint in script.")

def foo(a=def_value()):
    print(a)             #  a=def_value() jest uruchamiane podczas Compiling time i Runtime

                         # Kompilacja: Tłumaczenie kodu źródłowego na bajtkod → nie wykonuje funkcji, tylko analizuje ich składnię.
                         # Runtime: Wykonanie kodu, w tym obliczanie wartości domyślnych argumentów.




# def ops(a=): pass   # (Parsing Stage) SyntaxError: invalid syntax
