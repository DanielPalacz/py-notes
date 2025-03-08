from types import FunctionType

# class FunctionTypeExploration(FunctionType):
#     pass
# 'FunctionType' is marked as '@final' and should not be subclassed

# Definiujemy kod źródłowy funkcji
source_code = "def foo(): return 'Hello, world!'"

# Kompilujemy kod źródłowy do postaci kodu bajtowego
compiled_code = compile(source_code, filename="<string>", mode="exec")

# Tworzymy nowy słownik dla przestrzeni nazw funkcji
namespace = {}

# Uruchamiamy skompilowany kod, który zapisze funkcję `foo` w `namespace`
exec(compiled_code, namespace)

# Pobieramy obiekt kodu bajtowego dla funkcji `foo`
code_object = namespace["foo"].__code__

# Tworzymy nową funkcję przy użyciu FunctionType
new_function = FunctionType(code_object, globals())

# Wywołujemy nową funkcję
print(new_function())  # Hello, world!
