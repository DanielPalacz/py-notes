```
Mutowalność + +=

a = [1, 2, 3]
b = a
a += [4]

print(a)
print(b)


 - Czym to się różni od a = a + [4]?
 - Nowa struktura będzie stworzona, tzn nowe miejsce w pamięci - podczas, gdy: "a += [4]" nie utworzy nowej struktury.
 - Klasyczna pułapka, często w kodzie „in-place vs new object” może powodować niezamierzone side-effecty.
```

```
?
```