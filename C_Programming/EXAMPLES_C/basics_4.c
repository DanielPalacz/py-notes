#include <stdio.h>
#include <string.h>





int main(void)
{
    printf("CPython inheritance:\n");

    typedef struct {
        int a;
        int b;
    } Base;

    typedef struct {
        int a;
        int b;
        int c;
    } Derived;

    Derived d = {10, 20, 30};
    Base *p = (Base *)&d;
    printf(" - a = %d\n", p->a);
    printf(" - b = %d\n", p->b);
    // printf(" - c = %d\n", p->c);

    // Nie zmieniliśmy d.
    // Nie utworzyliśmy Base.
    // Nie skopiowaliśmy a ani b.
    // Po prostu powiedzieliśmy kompilatorowi:
    // „Traktuj adres d jako adres struktury Base.”
    // więc: p->a
    // oznacza: idź pod adres p + offset(a).

    printf("\n");
    printf("\n");


    // PyLongObject *x;
    // PyObject *obj = (PyObject *)x;

    // PyLongObject
    // ┌──────────────────┐
    // │ refcount         │ ← część wspólna (z PyObject)
    // │ type             │ ← część wspólna (z PyObject)
    // ├──────────────────┤
    // │ dane liczby      │ ← tylko PyLongObject
    // └──────────────────┘

    // Typ C wskaźnika 'PyObject *'' nie mówi nam, jaki konkretny typ obiektu Pythona znajduje się pod tym adresem.


    //                  PyObject *
    //                      │
    //                      ▼
    //              ┌───────────────┐
    //              │ ob_refcnt     │
    //              │ ob_type ──────┼──────► PyLong_Type
    //              ├───────────────┤
    //              │ digits        │
    //              │ ...           │
    //              └───────────────┘
    //                      ▲
    //                      │
    //                PyLongObject *

    // Czyli:
    //  - PyObject * mówi, jak możemy bezpiecznie patrzeć na początek obiektu.
    //  - ob_type mówi, jaki konkretnie typ Pythona reprezentuje obiekt.
    //  - A później możemy użyć tej informacji, żeby odpowiednio potraktować dalszą część pamięci.

    return 0;
}
