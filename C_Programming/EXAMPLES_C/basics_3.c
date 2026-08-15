#include <stdio.h>
#include <string.h>


void set_value(int *x)
{
    *x = 7;
}

void add_one(int *number)
{
    *number += 1;
}

void swap(int *a, int *b)
{
    int temp = *a; // odczyt przez de-referencje

    *a = *b;
    *b = temp;     // zapis przez de-referencje
}



int main(void)
{

    // 1

    // char x = 'a';       // -> 1 bajt
    // short x = 5;      // -> 2 bajty
    int x = 2;       // -> 4 bajty
    // long x = 1000;      // -> 8 bajtów
    // long long x = 1000; // -> 8 bajtów
    // float x = 1000;     // -> 4 bajty
    // double x = 1000;     // -> 8 bajtów
    // int x[10];          // zu -> 40 bajtów, zd -> 40, zx -> 28

    printf("1. sizeof(x):\n");
    printf(" - %zu\n", sizeof(x));
    printf(" - %zd\n", sizeof(x));
    printf(" - %zx\n", sizeof(x));

    printf("\n");
    printf("\n");


    // 2

    // printf("Adres zmiennej x: %p\n", &x);
    printf("2. Adres zmiennej x:\n - %p\n", (void *)&x);

    printf("\n");
    printf("\n");

    // 3

    int numbers[] = {11, 21, 31, 41};

    printf("3. Tablica 4 x int (+strlen/sizeof):\n");
    printf(" - tablice + pointer arithmetic\n");
    printf("\n");

    printf("0-element: %d\n", *(numbers + 0));
    printf("1-element: %d\n", *(numbers + 1));
    printf("2-element: %d\n", *(numbers + 2));
    printf("3-element: %d\n", *(numbers + 3));
    printf("0-element: %d\n", *(numbers));
    printf("\n");


    printf("%p\n", (void *)(numbers));
    printf("%p\n", (void *)(numbers + 0));
    printf("%p\n", (void *)(numbers + 1));
    printf("%p\n", (void *)(numbers + 2));
    printf("%p\n", (void *)(numbers + 3));
    printf("\n");

    char text1[] = "cat";
    printf("%zu\n", strlen(text1));
    char text2[] = "cat";
    printf("%zu\n", sizeof(text2));  // 6
    printf("\n");
    printf("\n");



    printf("4. functions:\n");
    printf(" - x=%d\n", x);
    set_value(&x);
    printf(" - x=%d\n", x);

    add_one(&x);
    printf(" - x=%d\n", x);
    add_one(&x);
    printf(" - x=%d\n", x);
    add_one(&x);
    printf(" - x=%d\n", x);
    add_one(&x);
    printf(" - x=%d\n", x);
    printf("\n");
    printf("\n");

    int xx = 10;
    int yy = 20;
//     printf("xx = %d\n", xx);
//     printf("yy = %d\n", yy);

    swap(&xx, &yy);

    printf("xx = %d\n", xx);
    printf("yy = %d\n", yy);
    printf("\n");
    printf("\n");

    printf("5. struct:\n");
    struct User {
        int age;
        double score;
    };


    struct User u1;
    struct User *ptr = &u1;

    u1.age = 11;
    u1.score = 99.0;
    printf(" - u.age = %d\n", u1.age);
    printf(" - u.score = %.1f\n", u1.score);

    ptr->age = 12;
    ptr->score = 98.0;
    printf(" - u.age = %d\n", u1.age);
    printf(" - u.score = %.1f\n", u1.score);
    printf("\n");
    printf("\n");


    printf("6. PyObject simulation:\n");

    typedef struct {
        char type;
    } PyTypeObject;

    typedef struct {
        int refcount;
        PyTypeObject *ob_type;
    } PyObject;


    PyTypeObject py_type_object;
    PyTypeObject *py_type_obj = &py_type_object;
    py_type_obj->type = 'a';

    PyObject py_object;
    PyObject *py_obj = &py_object;

    py_obj->refcount = 1;
    py_obj->ob_type = &py_type_object;
    printf(" - py_obj.refcount = %d\n", py_obj->refcount);
    printf(" - py_obj->ob_type = %p\n", (void *)py_obj->ob_type);

    return 0;
}
