#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// Wymaga: gcc -DNDEBUG basics2.c -o exec_basics2
//#if !defined(NDEBUG)
//#define DEBUG_MODE 1
//#else
//#define DEBUG_MODE 0
//#endif


struct Point {
    int x;
    int y;
};

struct Point p1; // W C zwykle musisz pisać struct Point, bo Point sam w sobie nie jest typem – dopóki nie użyjesz typedef.

void setPointValues(struct Point *p) {
    p->x = 101;
    p->y = 102;

    printf("   [setPoint] p->x: %d\n", p->x);
    printf("   [setPoint] p->y: %d\n", p->y);

}

void printXIntVarViaPointer(int *pointer) {
    printf("   [printXIntVarViaPointer] pointer = %p = &x - adres zmiennej x\n", pointer);
    printf("   [printXIntVarViaPointer] *pointer = %d = x            - wartość zmiennej x\n", *pointer);

}

void printIntTableViaPointer(int (*p)[3]) {
    printf("\n");
    printf("   [printIntTableViaPointer] pointer to numbers[3] = %p\n\n", p);
    printf("   [printIntTableViaPointer] (*p)[0] = %d - numbers[0], wartość zmiennej\n", (*p)[0]);
    printf("   [printIntTableViaPointer] (*p)[1] = %d - numbers[1], wartość zmiennej\n", (*p)[1]);
    printf("   [printIntTableViaPointer] (*p)[2] = %d - numbers[2], wartość zmiennej\n", (*p)[2]);

}




int x = 401;
int *px = &x;

int numbers[3] = {2, 5, 7};
int *p_numbers = numbers;
int (*p_table_numbers)[3] = &numbers;

int table[] = {11, 12, 13};

int main(void) {

    printf("1a - struct:\n");
    setPointValues(&p1);
    printf("   [main] p1.x: %d\n", p1.x);
    printf("   [main] p1.y: %d\n", p1.y);
    printf("\n");

    printf("1b - struct:\n");
    struct Point *p_struct = &p1;
    setPointValues(p_struct);
    printf("\n\n");

    // Zadanie: napisz program, który wypisuje adres zmiennej i jej wartość przez wskaźnik.
    printf("2 - Zadanie: napisz program, który wypisuje adres zmiennej i jej wartość przez wskaźnik:\n");
    printf("   [main] px = %p = &x - adres zmiennej x\n", px);
    printf("   [main] *px = %d = x            - wartość zmiennej x\n\n", *px);

    printXIntVarViaPointer(px);
    printf("\n   [main] numbers = %p = - adres zmiennej numbers\n", numbers);


//    if (DEBUG_MODE) {
//        raise(SIGTRAP); // wysyła SIGTRAP, debugger zatrzymuje się (można kontynuować)
//    }

    printIntTableViaPointer(p_table_numbers);
    // __builtin_trap(); // generuje nielegalną instrukcję — system natychmiast kończy proces (__builtin_trap() całkowicie przerywa program)
    printf("\n   [main] END\n");

    return 0;
}
