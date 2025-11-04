# Typy i paradygmaty w Pythonie

```
Brak typów prostych i to, że wszystko jest obiektem, mówi wiele o filozofii Pythona:

Obiektowość (OOP)
 - Python jest w pełni obiektowy: każda wartość jest instancją jakiejś klasy.
 - Typy takie jak int, str, list to po prostu klasy wbudowane.

Abstrakcja i spójność modelu
 - Skoro wszystko jest obiektem, to można z każdym obiektem postępować w ten sam sposób: wywoływać metody, przypisywać, przekazywać jako argumenty, itp.

Elastyczność i metaprogramowanie
 - Obiekty można modyfikować w locie, introspekować (type(), dir(), getattr()), dynamicznie tworzyć klasy, itp.

Paradygmaty:
 - Obiektowy (klasy, dziedziczenie, metody)
 - Imperatywny (instrukcje, pętle, przypisania)
 - Funkcyjny (funkcje wyższego rzędu, map, filter, lambda)
 - Dynamiczny ~ dynamicznie typowany ~ (typy, wiązanie nazw)

Model typów w Pythonie – w skrócie:
 - Wszystko jest obiektem (nawet liczby i None).
 - Brak typów prostych = spójny, obiektowy model danych.
 - Typ jest własnością wartości, nie zmiennej.
 - Python jest silnie i dynamicznie typowany. Silne typowanie oznacza, że interpreter nie konwertuje typów „po cichu” (np. nie połączy int z str bez jawnego przekształcenia).
   Natomiast np. JavaScript jest słabo i dynamicznie typowany a C jest statycznie i silnie typowanym językiem (choć z pewnymi niuansami).
   W praktyce C jest czasem określany jako „średnio silnie typowany” — bo pozwala na jawne i niekiedy niebezpieczne konwersje typów (rzutowania, czyli casts).
   
 - Język wieloparadygmatowy: obiektowy, imperatywny, funkcyjny.
 - Filozofia: „W Pythonie wszystko ma typ i wszystko jest obiektem (spójny, obiektowy model typów).”

W skrócie – co z tego wynika praktycznie:
 - Nie musisz deklarować typów -> szybko prototypujesz.
 - Nie można bezkarnie mieszać typów -> Python broni spójności.
 - Możesz introspektować obiekty i dynamicznie nimi manipulować → bardzo elastyczny język.
 - Rozumiesz, dlaczego int to klasa, a nie "goły typ liczbowy" (to wynika z filozofii Pythona).
```
