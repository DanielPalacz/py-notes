#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


int click_anything() {
    printf("\n\n[Click anything and press Enter]\n");

    getchar(); // Pobiera znak wpisany przez użytkownika

    // NOWOŚĆ: Czyszczenie bufora z Entera (\n), który został po wpisaniu znaku
    int b;
    while ((b = getchar()) != '\n' && b != EOF);

    return 0;
}


int click_enter() {

    printf("\n\n[Click enter]\n");
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    return 0;

}



int print_example2() {
    printf("\n\n2) (Liczymy) Obwód prostokąta.\n");

    float dlugosc, szerokosc, obwod;

    printf("Podaj dlugosc prostokata: ");
    scanf("%f", &dlugosc);

    printf("Podaj szerokosc prostokata: ");
    scanf("%f", &szerokosc);

    obwod = 2 * (dlugosc + szerokosc);
    int calkowita_obwod = (int)obwod;
    float dziesietna = obwod - calkowita_obwod;

    if (dziesietna > 0) {
        printf("Obwod prostokata: %.1f\n", obwod);
    } else {
        printf("Obwod prostokata: %d\n", calkowita_obwod);
    }

    return 0;

}





int main(void) {
    printf("\nPodstawy w C:\n");
    print_example2();

    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}