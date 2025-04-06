class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A):
    pass

obj = C()
print(obj.greet())  # Powinno zwrócić: "Hello from A"

# Zmieniamy dziedziczenie
C.__bases__ = (B,)

# Sprawdźmy MRO
print(C.mro())  # Powinno zwrócić: [C, B, object]

# Ponownie wywołujemy greet()
print(obj.greet())  # Powinno zwrócić: "Hello from B"
