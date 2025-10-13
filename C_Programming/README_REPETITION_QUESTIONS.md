
#### README_REPETITION_QUESTIONS

```
1. Jaki jest pełny flow kompilacji-budowania-uruchamienia programu napisanego w C?
2. Do czego wykorzystywany jest stos w C? A do czego sterta?
3. Jakie są podstawowe typy danych w C? Podstawowe typy a także przykłady złożonych typów.
4. Jak działają wskaźniki? Jak np działa proste przypisanie przez wskaźnik?
5. Tablica jest ciągłym blokiem zarezerwowanej pamięci - nie jest wskaźnikiem. Z tego wynikają niuanse podczas korzystania z tablic.
6. Zmienna globalna a dyrektywa preprocesora?
```


```
Ad.1)
Narzędzie kompilacyjne / kompilator GNU C (GCC).
Pełny flow kompilacji-budowania-uruchomienia programu napisanego w C.

gcc hello_world.c -o hello
    tak naprawdę dzieje się kilka etapów (GCC ukrywa je w jednym kroku):

a)
 - gcc -E hello_world.c -o hello_world.i (Preprocesor, cpp)
   Preprocesor patrzy na dyrektywy takie jak: #include, #define, #if.
   Cały kod nagłówka stdio.h zostaje wklejony (to są deklaracje m.in. printf).
   Rezultat: powstaje czysty kod źródłowy w C bez dyrektyw #include.

b)
 - gcc -S hello_world.c -o hello_world.s (Kompilacja/kompilator, cc1)
   Kod w C zostaje przetłumaczony na asembler (czyli niskopoziomowe instrukcje dla procesora). Rezultat: plik .s

c)
 - gcc -c hello_world.c -o hello_world.o (Asemblacja, as)
   Asembler tłumaczy plik .s na kod maszynowy (bajty zrozumiałe dla CPU). Rezultat: plik obiektowy .o (np. hello_world.o).


d)
 - Linkowanie (Linkowanie statyczne odbywające się w czasie kompilacji, ld)
   Twój program potrzebuje jeszcze bibliotek (np. printf nie jest wbudowany).
   Linker łączy twój kod (hello_world.o) z biblioteką standardową C (libc.so).
   Rezultat: plik wykonywalny hello w formacie ELF (Executable and Linkable Format).

e)
 - Uruchomienie (./hello)
   System ładuje program do pamięci (dzięki loaderowi).
   Ustawiany jest stos, zmienne środowiskowe, argumenty programu.
   Wywoływana jest funkcja main() w twoim kodzie.
   Po zakończeniu, wynik (return 0;) jest przekazywany do systemu operacyjnego jako kod wyjścia procesu.
```

##### [Listen to the recording](audio-file1.mp3)
