#include <stdio.h>
#include <stdlib.h>

// Zmienna globalna (bez inicjalizacji) → segment BSS
int g_uninitialized;

// Zmienna globalna (z inicjalizacją) → segment danych (data segment)
int g_initialized = 42;

int main(void) {
    // Zmienna lokalna → stos (stack)
    int local = 1;

    // Zmienna statyczna lokalna → segment danych (data segment)
    static int s_local = 2;

    // Zmienna dynamiczna → sterta (heap)
    int *heap_var = malloc(sizeof(int));
    *heap_var = 3;

    printf("Adres kodu programu (funkcja main):   %p\n", (void *)main);
    printf("Adres globalnej zainicjalizowanej:    %p\n", (void *)&g_initialized);
    printf("Adres globalnej niezainicjalizowanej: %p\n", (void *)&g_uninitialized);
    printf("Adres statycznej lokalnej:            %p\n", (void *)&s_local);
    printf("Adres na stercie (malloc):            %p\n", (void *)heap_var);
    printf("Adres zmiennej lokalnej:              %p\n", (void *)&local);

    free(heap_var);
    return 0;
}
