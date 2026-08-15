#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>




int print_example3() {
    printf("\n\n3) Tablice, tablica liczb\n");
    printf("Inicjalizacja samej tablicy: liczby[5]\n");
    int liczby[5]; // tablica 5 elementów typu int
    int mem_size = sizeof(liczby);
    printf("Tablica 'liczby', ilość bajtów w pamięci: %d", mem_size);


    printf("\n");
//     char c;
//     scanf("%c", &c);
//     if (c == '\n') {
//         printf("Napisz cokolwiek, np. Enter.");
//         scanf("%c", &c);
//     }

    // przypisanie elementów
    printf("Przypisanie elementów do tablicy liczby:\n");
    for (int i = 0; i < 5; i++) {
        liczby[i] = i + i + i;
    }

    // liczby[5] = 55; // undefined behavior w C - brak błędu
    // liczby[6] = 66; // stack smashing

    printf("\nWypisanie elementów:\n");
    // wypisanie elementów
    for (int i = 0; i < 5; i++) {
        printf("liczby[%d] = %d\n", i, liczby[i]);
    }
    return 0;

}



int main(void) {
    printf("\nPodstawy w C:\n");
    print_example3();

    //
    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}