#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


int print_example1() {
    printf("\n\n1) Pole prostokąta.\n");
    float dlugosc = 1.3;
    float szerokosc = 2.2;
    float pole;

    pole = dlugosc * szerokosc;
    printf("Pole prostokata: %.1f\n", pole);

    return 0;
}

int print_example2() {
    printf("\n\n2) Obwód prostokąta (rzutowanie float na int).\n");

    float dlugosc, szerokosc, obwod;

    printf("Podaj dlugosc prostokata: ");
    scanf("%f", &dlugosc);

    printf("Podaj szerokosc prostokata: ");
    scanf("%f", &szerokosc);

    obwod = 2 * (dlugosc + szerokosc);
    int calkowita = (int)obwod;
    float dziesietna = obwod - calkowita;

    if (dziesietna > 0) {
        printf("Obwod prostokata: %.2f\n", obwod);
    } else {
        printf("Obwod prostokata: %.1f\n", obwod);
    }

    return 0;

}


int print_example3() {
    printf("\n\n3) Tablice, tablica liczb\n");
    printf("inicjalizacja samej tablicy liczby[5]...\n");
    int liczby[5]; // tablica 5 elementów typu int
    int mem_size = sizeof(liczby);
    printf("'liczby' ilość bajtów w pamięci: %d\n", mem_size);

    // przypisanie elementów
    printf("przypisanie elementów do tablicy liczby...\n");
    for (int i = 0; i < 5; i++) {
        liczby[i] = i + i + i;
    }

    // liczby[5] = 55; // undefined behavior w C - brak błędu
    // liczby[6] = 66; // stack smashing

    printf("wypisanie elementów:\n");
    // wypisanie elementów
    for (int i = 0; i < 5; i++) {
        printf("liczby[%d] = %d\n", i, liczby[i]);
    }
    return 0;

}


int print_size_f() {
    printf("\n\n4) Rozmiar struktur:\n");
    printf("Rozmiar int: %zu bajtów\n", sizeof(int));
    printf("Rozmiar tablicy 5 elementów: %zu bajtów\n", sizeof(int)*5);
    return 0;
}

int print_example5() {
    printf("\n\n5) Iteracja po znakach aż do \\0.\n");

    char str[] = "Hello, C!";
    // Iteracja po znakach aż do '\0'
    for (int i = 0; str[i] != '\0'; i++) {
        printf("Znak na pozycji %d: %c\n", i, str[i]);
    }

    return 0;

}

int print_example6() {
    printf("\n\n6) Wskaźniki, wstęp.\n");

    int x = 10;
    int *ptr = &x; // wskaźnik ptr przechowuje adres x

    printf("x = %d\n", x);
    printf(" -> Deklaracja wskaźnika: int *ptr = &x;\n");
    printf(" -> // wskaźnik ptr przechowuje adres x");
    printf("Adres x = %p\n", &x);
    printf("ptr (adres zmiennej x) = %p\n", ptr);
    printf("&ptr (adres wskaźnika ptr) = %p\n", &ptr);
    printf("Wartosc wskazywana przez ptr = %d\n", *ptr);
    printf("\n\n");

    return 0;
}





int repeat_knowledge_A() {
      int x1 = 2;
      x1 = 3; // też na stosie
      // Kompilator C generuje kod odkładający zmienne lokalne i adresy powrotu właśnie na stosie.

      printf("\n\nRepetition A (liczby int, scanf, printf, stos w C):");
      printf("\n * x1=%d\n", x1);
      int x2;
      printf(" * podaj wartosc x2: ");
      scanf("%d", &x2);
      printf(" * zatem x2=%d\n", x2);

      if (x2 == 101) {
            printf(" * funkcja repeat_knowledge_A zwróci %d\n", x2);
      }
      else {
            printf(" * funkcja repeat_knowledge_A nie zwróci 101");
      }

      return x2;
}


int repeat_knowledge_B() {
      printf("\n\nRepetition B (przypisanie przez wskaźnik):\n");
      int y2;
      int *b2 = &y2;
      printf(" * podaj wartosc y2: ");
      scanf("%d", b2);
      printf(" * zatem y2=%d (wskaźnik b2 użyty)\n", y2);

      return 102;
}


int repeat_knowledge_C() {
      printf("\n\nRepetition C (wskaźnik a tablica):\n");

      // Na systemie 64-bitowym, gdzie sizeof(int) == 4 i wskaźnik ma 8 bajtów:
      int liczby[5];
      int size1 = sizeof(liczby);
      //→ rozmiar całego bloku tablicy
      //→ 5 * 4 = 20
      printf(" * rozmiar całego bloku tablicy: %d bajtów\n", size1);

      int size2 = sizeof(&liczby);
      //→ „adres całej tablicy” – to jest wskaźnik do tablicy 5 elementów
      //→ rozmiar wskaźnika → 8
      printf(" * adres całej tablicy, to jest wskaźnik do tablicy 5 elementów - rozmiar: %d bajtów\n", size2);

      int size3 = sizeof(&liczby[0]);
      //→ adres pierwszego elementu – zwykły wskaźnik na int
      //→ rozmiar wskaźnika → 8
      printf(" * adres pierwszego elementu – zwykły wskaźnik na int, rozmiar: %d bajtów\n", size3);

      int size4 = sizeof(*liczby);
      //→ *liczby to dereferencja pierwszego elementu, czyli int
      //→ 4
      printf(" * *liczby to dereferencja pierwszego elementu, czyli int, rozmiar: %d bajtów\n", size4);

      return 103;
}

// Dyrektywy preprocesora (działa zanim kod trafi do kompilatora).
// Preprocesor w C nie wykonuje kodu, tylko przygotowuje kod do kompilacji.
#define SIZE 5
#define PI 3.14159
#define HELLO "Cześć!"
const double PI2 = 3.14159; // prawdziwa zmienna globalna o typie double
int licznik = 0;  //  prawdziwa zmienna globalna o typie int


int repeat_knowledge_D() {
      printf("\n\nRepetition D (preprocesor #define impact):\n");

      int tab[SIZE];   // tutaj kompilator naprawdę zobaczy int tab[5];
      printf("Rozmiar = %d\n", SIZE);

      return 104;
}



int repeat_knowledge_E() {
      printf("\n\nRepetition E:\n");
      printf(" * tablica jest ciągłym blokiem zarezerwowanej pamięci - nie jest wskaźnikiem\n");
      printf(" * int (*p)[3] = &numbers;  // wskaźnik na tablicę 3 int\n");
      int numbers[3];
      int (*p)[3] = &numbers;  // wskaźnik na tablicę 3 intów
      (*p)[0] = 20;
      (*p)[1] = 21;
      (*p)[2] = 22;
      printf(" * numbers[0],...: %d, %d, %d\n\n", numbers[0], numbers[1], numbers[2]);

      return 105;
}



char* slice(const char *src, int start, int end) {
    // obliczamy długość "wycinka"
    int len = end - start;
    if (len <= 0) return NULL;

    // rezerwujemy pamięć (len znaków + terminator '\0')
    char *result = malloc(len + 1);
    if (!result) return NULL;

    // kopiujemy fragment ze src[start] przez len znaków
    strncpy(result, src + start, len);
    result[len] = '\0';  // ręczne zakończenie

    return result;
}



int strlen_f(const char *word, bool debug) {
    int i = 0;
    while (word[i] != '\0') {
        if (debug) {
            printf("[strlen_f body]: Znak nr %d (%c)\n", i, word[i]);
        }
        i++;
    }
    return i;
}

//int strlen_f(const char *word, bool debug) {
//    const char *p = word;   // wskaźnik startuje na początek napisu
//
//    while (*p != '\0') {    // dopóki nie trafimy na terminator
//        if (debug) {
//            printf("[strlen_f ptr]: Znak (%c)\n", *p);
//        }
//        p++;                // przesuwamy wskaźnik na kolejny znak
//    }
//
//    return p - word;        // różnica adresów = liczba znaków
//}


// gcc day2.c -o day2; ./day2 < IN.TXT
// cat IN.TXT | ./day2
// echo -e "2\n3.11\n" | ./day2
// wszystkie trzy wywołania działają, bo Linux/Unix traktuje stdin jako abstrakcyjny strumień wejściowy

int main(void) {
      printf("\nPodstawy w C:\n");

      print_example1();
      print_example2();
      print_example3();
      print_size_f();
      print_example5();
      print_example6();

      repeat_knowledge_A();
      repeat_knowledge_B();
      repeat_knowledge_C();


      // 04.09
      repeat_knowledge_D();
      repeat_knowledge_E();
      printf("[strlen_f output]: %d\n\n\n", strlen_f("akdehwklhejher", false));

      // compiled program returns the following value to shell process, it can be read by 'echo $?'
      return 9;
}
