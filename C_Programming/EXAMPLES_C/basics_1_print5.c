#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


int print_example5() {
    printf("\n\n5) Iteracja po znakach aż do \\0.\n");

    char str[] = "Hello!";
    // Iteracja po znakach aż do '\0'
    for (int i = 0; str[i] != '\0'; i++) {
        printf("Znak na pozycji %d: %c\n", i, str[i]);
    }

    return 0;

}






int main(void) {
    printf("\nPodstawy w C:\n");
    print_example5();

    printf("\n\n");
      // the following value to shell process, it can be read by 'echo $?'
    return 201;
}