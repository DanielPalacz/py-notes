

# INTRO_TO_C:


##### Flow budowania / uruchomienia programu
```
 - gcc -E hello_world.c -o hello_world.i (Preprocesor, cpp, # - ten znak w kodzie C oznacza preprocesor)
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
 - tablica, typ złożony definiujący ciągły blok zarezerwowanej pamięci - nie wskaźnik.
 - wskaźnik, typ złożony przechowujący adres w pamięci innej zmiennej

Tablice:
    char text[] = "Hello, C!"; // tablica elementów typu char
    int liczby[5]; // tablica 5 elementów typu int

Wskaźniki:
    int a1 = 11;
    int *p = &a1;
        // *p - wartosc wskazywana przez wskaźnik, wartość 'a1'
        // p - adres w pamięci, gdzie jest  ulokowana wskazywana zmienna 'a'
        // &p - adres w pamięci, gdzie jest  ulokowany wskaźnik p
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

+-------------------------------+  <--- niskie adresy
|   Kod programu (text)         |   instrukcje maszynowe (tylko do odczytu), funkcje, main(), itp
+-------------------------------+
|   Dane statyczne (data)       |   globalne, static, stałe tablice
|   - zainicjalizowane          |   BSS (Block Started by Symbol)
|   - niezainicjalizowane (bss) |   zmienne globalne lub statyczne, które nie zostały jawnie zainicjalizowane (albo zainicjalizowane na zero)  
+-------------------------------+
|           Heap                |   malloc/calloc/realloc
|           (sterta)            |   rośnie "w górę" (ku wyższym adresom)
|                               |
|                               |
|    [wolna przestrzeń]         |
|                               |
|                               |
|           Stack               |   zmienne lokalne, ramki funkcji
|           (stos)              |   rośnie "w dół" (ku niższym adresom)
+-------------------------------+   <--- wysokie adresy


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


```
Schemat pamięci procesu - jeszcze raz:


                 ↑  rośnie ku WYŻSZYM adresom
                 │
                 │
   +---------------------------------------------+
   |                 Stos (Stack)                |
   |---------------------------------------------|
   |  zmienne lokalne funkcji, adresy powrotu    |
   |  przykład: local → 0x7ffe53dd9d6c           |
   |                                             |
   |  rośnie W DÓŁ (ku niższym adresom)          |
   +---------------------------------------------+
   |           [wolna przestrzeń RAM procesu]    |
   +---------------------------------------------+
   |                 Sterta (Heap)               |
   |---------------------------------------------|
   |  pamięć dynamiczna (malloc, free, new, itd.)|
   |  przykład: malloc → 0x62a9b42872a0          |
   |                                             |
   |  rośnie W GÓRĘ (ku wyższym adresom)         |
   +---------------------------------------------+
   |             Dane statyczne (Data)           |
   |---------------------------------------------|
   |  globalne i statyczne zmienne programu      |
   |   g_initialized → 0x62a9a5053010            |
   |   s_local (static) → 0x62a9a5053014         |
   |   g_uninitialized (BSS) → 0x62a9a505301c    |
   +---------------------------------------------+
   |           Kod programu (Text)               |
   |---------------------------------------------|
   |  instrukcje maszynowe, np. main()           |
   |  przykład: main → 0x62a9a50501a9            |
   |  tylko do odczytu i wykonywania             |
   +---------------------------------------------+
                 │
                 │
                 ↓  niższe adresy

```

#### PODSTAWOWE KOMENDY GDB:
```
gdb programCompiledByGcc

(gdb) run // uruchamia program od początku
(gdb) bt // stos wywołań (stack trace) — czyli ścieżkę funkcji, które doprowadziły do bieżącego miejsca
      up / down - poruszanie się po stosie wywołań
(gdb) list
(gdb) list main
(gdb) list 10,20
(gdb) info locals
(gdb) info registers
(gdb) print x
$1 = 42
(gdb) p y + 3
$2 = 7

break (lub b) - ustawia breakpointa w określonym miejscu. Po tym, gdy dasz run, program zatrzyma się w tym miejscu.
(gdb) break main
(gdb) break 25
(gdb) break my_function

next i step - Krokowe wykonanie kodu:
next (lub n) → przechodzi do następnej linii (nie wchodzi do funkcji)
step (lub s) → przechodzi do następnej linii wchodząc do funkcji

continue (lub c) - wznawia wykonanie programu po zatrzymaniu (np. po breakpoincie).
(gdb) continue


Musisz skomplikować program z flagą debugową -g, np.:
gcc -g exec_basics2.c -o exec_basics2
 - dodaje do binarki symbole debugowe (informacje o nazwach funkcji, liniach, zmiennych),
 - ale nie wpływa na działanie programu
 - wtedy: "list" i "info locals" zadziałają ...
```