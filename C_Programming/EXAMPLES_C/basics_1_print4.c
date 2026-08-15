#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>



int print_example4() {
    printf("\n\n4) Powtórka, tablice, liczby.\n");
    printf("Zainicjujesz teraz tablicę liczb (int) o pewnym rozmiarze - jakim? Zdecyduj teraz?\n");
    printf("\n");

    int rozmiar;
    printf("Podaj rozmiar tablicy: ");
    scanf("%d", &rozmiar);

    int liczby[rozmiar];
    int mem_size = sizeof(liczby);
    printf("Tablica 'liczby' - ilość bajtów w pamięci: %d\n", mem_size);


    // Przypisanie elementów
    printf("Przypisanie elementów do tablicy liczby.\n");
    for (int i = 0; i < rozmiar; i++) {
        liczby[i] = i + i + i + i;
    }

    printf("\nWypisanie elementów:\n");
    // wypisanie elementów
    for (int i = 0; i < rozmiar; i++) {
        printf("liczby[%d] = %d\n", i, liczby[i]);
    }

    return 0;

}




int main(void) {
    printf("\nPodstawy w C:\n");
    print_example4();

    //
    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}