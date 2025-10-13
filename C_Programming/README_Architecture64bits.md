

##### "Architektura 64-bitowa"


```
W uproszczeniu "Architektura 64-bitowa" oznacza, że rejestry procesora (w tym rejestry adresowe) mają 64 bity, czyli:
 - Adres w pamięci można zapisać jako liczbę 64-bitową.

Każdy adres zajmuje 8 bajtów (64 bity / 8 = 8 bajtów).
Ale jest ważny praktyczny szczegół:
    Procesory x86-64 (czyli np. AMD64, Intel 64) nie wykorzystują wszystkich 64 bitów do adresowania.
    Obecnie zwykle implementowane jest 48 lub 57 bitów przestrzeni adresowej (np. w tzw. canonical addresses).
    Reszta bitów musi mieć określone wartości, żeby adres był ważny.
```