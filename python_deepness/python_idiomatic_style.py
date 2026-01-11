"""
Python idiomatic style
    Czytelność, prostota, zaufanie do obiektów, idiomatyczne użycie Pythona, minimalizacja boilerplate.
    Duck typing jest tu kluczowym elementem, bo pozwala pisać idiomatyczny kod działający na różnych typach obiektów.
"""

# 1. Duck Typing & EAFP
#    Zasada: „Nie pytaj o typ, tylko używaj tego, co obiekt potrafi” (Easier to Ask for Forgiveness than Permission).

def print_length(obj):
    try:
        print(len(obj))
    except TypeError:
        print("Object has no length")

# Dlaczego Pythonic: kod jest elastyczny, nie sprawdza typu obiektu wprost.


# 2. List comprehensions / Generator expressions
#    Zasada: zwięzłe, czytelne iteracje i transformacje danych.

squared = [x**2 for x in range(10)]
even_gen = (x for x in range(10) if x % 2 == 0)

# Dlaczego Pythonic: unika nadmiarowych pętli for, zwiększa czytelność i wydajność (generatory).


# 3. Context Managers (with)
#    Zasada: automatyczne zarządzanie zasobami (pliki, połączenia sieciowe, locki).

with open("data.txt", mode="t+w") as f:
    data = f.read()

# Dlaczego Pythonic: gwarantuje zwolnienie zasobów, czytelny blok działania.


# 4. Idiom „Pythonic unpacking”
#    Zasada: zwięzłe przypisania wielu wartości, destrukturyzacja.

a, b, *rest = [1, 2, 3, 4, 5]

# Dlaczego Pythonic: czytelność, zwięzłość, brak ręcznego indeksowania.


# 5. Walidacja i błędy przez wyjątki zamiast if-ów
#    Zasada: EAFP zamiast LBYL (Look Before You Leap).

try:
    my_dict = {"a": "a1"}
    value = my_dict['key']
except KeyError:
    value = None

# Dlaczego Pythonic: kod jest bardziej naturalny dla dynamicznego typowania, krótszy i czytelny.


# 6. Unikanie nadmiarowych getterów/setterów
#    Zasada: używaj property zamiast jawnych metod.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

# Dlaczego Pythonic: prostszy, czytelny interfejs, bez nadmiarowego boilerplate’u.


# 7. Zen of Python
# import this


# 8. Idiom enumerate / zip
#    Zasada: zwięzła iteracja z indeksami lub równoległe iteracje.
my_list = [1, 2, 3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

for i, val in enumerate(my_list):
    print(i, val)

for x, y in zip(list1, list2):
    print(x, y)

# Dlaczego MID: poprawia czytelność, zmniejsza błędy przy indeksowaniu ręcznym.


# 9. Minimalizm i brak nadmiarowych warunków
#    Zasada: kod powinien być prosty, unikać „na wszelki wypadek”.


# złe
if len(my_list) > 0:
    first = my_list[0]

# Pythonic
if my_list:
    first = my_list[0]

