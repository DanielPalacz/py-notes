

# INTRO_TO_C:


##### Flow budowania / uruchomienia programu
```
 - gcc -E hello_world.c -o hello_world.i (Preprocesor, cpp)
 - gcc -S hello_world.c -o hello_world.s (Kompilacja (cc1)
 - gcc -c hello_world.c -o hello_world.o (Asemblacja, as)
 - gcc hello_world.c -o hello_world.o (ld, Linkowanie statyczne odbywa się w czasie kompilacji)

 - gcc hello_world.c -o hello; ./hello (Uruchomienie):
 
 
Compiling with debug symbols and gdb debugger usage:
 - gcc -g main.c -o main
 - gdb ./main
 - (gdb) run
 - TO EXTEND KNOWLEDGE IN SOME DAY
```

### Typy danych w języku C:
```
Typy podstawowe (scalar types):

 - int (i jego warianty: short, long, long long, ze znakiem/signed, bez znaku/unsigned).
 - char (signed char, unsigned char też istnieją).
 - float, double, long double.
 - _Bool (od C99).
 - void (brak wartości).

Typy złożone:
 - Tablica (np. int arr[10])
 - Wskaźnik (np. int *p)
 - Struktura (struct)
 - Unia (union), Wyliczenie (enum)

W języku C: NULL i sentinele to konwencje, nie oddzielne typy danych.

Czym różni się tablica od wskaźnika?
 - tablica jest ciągłym blokiem zarezerwowanej pamięci - nie jest wskaźnikiem
```

#### Zakresy (scopes) w C:
```
 - Globalny zakres
 - Zakres funkcji (lokalny, parametry funkcji to też lokalny zakres)
 - Zakres bloków

Brak "enclosing scopes" - dlatego w C jest prostszy system zakresów niż Pythonie.
```


#### Stos vs Sterta vs Schemat pamięci procesu:
```
 - Stos: pamięć procesu, działa LIFO, kompilator odkłada tam zmienne lokalne i adresy powrotu.
 - Sterta: osobny obszar pamięci, do dynamicznej alokacji (malloc, free).
 - i jeszcze: data segment (dane statyczne) i "text segment" (kod programu)

+-----------------------------+  <--- niskie adresy
|   Kod programu (text)       |   instrukcje maszynowe (tylko do odczytu)
+-----------------------------+
|   Dane statyczne (data)     |   globalne, static, stałe tablice
|   - zainicjalizowane        |
|   - niezainicjalizowane     |
+-----------------------------+
|           Heap              |   malloc/calloc/realloc
|           (sterta)          |   rośnie "w górę" (ku wyższym adresom)
|                             |
|                             |
|    [wolna przestrzeń]       |
|                             |
|                             |
|           Stack             |   zmienne lokalne, ramki funkcji
|           (stos)            |   rośnie "w dół" (ku niższym adresom)
+-----------------------------+  <--- wysokie adresy


Tablice, przykłady:

    char global_name[20];   // data segment
    
    int main(void) {
        char local[20];         // stos
        static char buffer[20]; // data segment
        char *dyn = malloc(20); // sterta
        scanf("%s", global_name); // data segment
    
        printf("global_name: %s\n", global_name);
    }
```
