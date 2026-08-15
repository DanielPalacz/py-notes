#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>



int print_example6() {
    printf("\n\n6) Wskaźniki, wstęp.\n");
    printf("\n");

    int x = 10;
    int *ptr = &x; // wskaźnik ptr przechowuje adres x

    printf("x = %d\n", x);

    printf(" -> Deklaracja wskaźnika: int *ptr = &x;\n");
    printf(" -> // wskaźnik ptr przechowuje adres x\n");
    printf("\n");
    printf("Adres x = %p\n", &x);
    printf("ptr (adres zmiennej x) = %p\n", ptr);
    printf("&ptr (adres wskaźnika &ptr) = %p\n", &ptr);
    printf("Wartosc wskazywana przez ptr = %d\n", *ptr);
    printf("\n\n");

    return 0;
}





int main(void) {
    printf("\nPodstawy w C:\n");
    print_example6();

    //
    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}