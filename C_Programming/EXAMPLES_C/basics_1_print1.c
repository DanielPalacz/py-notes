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


int print_example1a() {
    click_anything();
    click_enter();

    printf("\n\n1a) Pole prostokąta (11, 22).\n");
    int dlugosc = 11;
    int szerokosc = 22;
    int pole;

    pole = dlugosc * szerokosc;
    printf("Pole prostokata: %d\n", pole);

    return 0;
}


int print_example1b() {
    printf("\n\n1b) Pole prostokąta  (1.3, 2.2).\n");
    float dlugosc = 1.3;
    float szerokosc = 2.2;
    float pole;

    pole = dlugosc * szerokosc;
    printf("Pole prostokata: %.1f\n", pole);

    return 0;
}


int print_example1c() {
    printf("\n\n1c) Pole prostokąta (13, 2.2).\n");
    int dlugosc = 13;
    float szerokosc = 2.2;
    float pole;

    pole = dlugosc * szerokosc;
    printf("Pole prostokata: %.1f\n", pole);

    return 0;
}


int print_example1d(const int dlugosc) {
    printf("\n\n1d) Pole prostokąta (%d, 22).\n", dlugosc);
    int szerokosc = 22;
    int pole;

    pole = dlugosc * szerokosc;
    printf("Pole prostokata: %d\n", pole);

    return 0;
}





int main(void) {
    printf("\nPodstawy w C:\n");

    print_example1a();
    print_example1b();
    print_example1c();
    print_example1d(4);


    //
    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}