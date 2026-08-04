import weakref

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} został usunięty")

p = Person("Jan")

# Tworzymy słabą referencję
weak_p = weakref.ref(p)

print(weak_p())        # <__main__.Person object at ...>
print(weak_p().name)   # Jan

# Usuwamy jedyną silną referencję
del p

# Obiekt został zniszczony
print(weak_p())        # None


# p  ─────────────► Person("Jan")   ← silna referencja
#
# weak_p ─ ─ ─ ─ ► Person("Jan")    ← słaba referencja



# import weakref
#
# class Image:
#     def __init__(self, filename):
#         self.filename = filename
#
# cache = weakref.WeakValueDictionary()
#
# img = Image("photo.jpg")
# cache["photo"] = img
#
# print(cache["photo"].filename)   # photo.jpg
#
# del img
#
# print(dict(cache))               # {}

# WeakValueDictionary sam usuwa wpis, gdy wartość (obiekt Image) zostanie zniszczona.



# Najważniejsze elementy modułu
# weakref.ref(obj) – tworzy słabą referencję.
# weakref.WeakValueDictionary – słownik ze słabymi referencjami do wartości.
# weakref.WeakKeyDictionary – słownik ze słabymi referencjami do kluczy.
# weakref.WeakSet – zbiór przechowujący obiekty jako słabe referencje.
#
# weakref jest szczególnie przydatny przy implementacji:
#  - cache'ów,
#  - rejestrów obiektów,
#  - obserwatorów (Observer pattern)
#  - oraz w sytuacjach, gdy chcemy uniknąć cykli referencji lub nie chcemy sztucznie przedłużać życia obiektów.
