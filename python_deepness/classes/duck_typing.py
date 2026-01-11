"""
Duck typing odnosi się do metafory mówiącej:
 - jeśli coś się zachowuje jak kaczka, to prawdopodobnie jest kaczką
 - przenosząc to na Pythona mówi się, że nie liczy się dziedziczenie klas, lecz interfejs/metody dostępne w obiekcie
 - duck typing w praktyce pozwala używać obiektu w funkcji, jeśli ma odpowiednie metody, niezależnie od tego,
   czy dziedziczy po jakiejkolwiek klasie
 - duck typing pozwala pisać bardziej elastyczne funkcje i klasy
 - pozwala używać różnych typów obiektów bez wymuszania dziedziczenia
 - wymaga uważnej dokumentacji i testów

Duck typing to styl programowania mieszczący się w tak zwanym "Pythonic thinking".
"""

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack too!")

def make_it_quack(entity):
    entity.quack()  # nie sprawdzamy typu, tylko metodę

