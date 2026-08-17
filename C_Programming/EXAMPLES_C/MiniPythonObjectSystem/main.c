#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct TypeObject {
    const char *name;
} TypeObject;


TypeObject IntType = {
    .name = "int"
};


typedef struct {
    size_t refcnt;
    struct TypeObject *type;
} Object;


typedef struct {
    Object base;
    long value;
} IntObject;



IntObject* new_int(long number) {

    Object obj;
    obj.type = NULL;

    IntObject *p = malloc(sizeof(IntObject));
    p->base = obj;
    p->base.type = &IntType;
    p->value = number;
    p->base.refcnt = 1;

    return p;

}


void Py_DECREF(Object *obj)
{
    obj->refcnt--;

    if (obj->refcnt == 0) {
        free(obj);
    }
}

void Py_INCREF(Object *obj)
{
    obj->refcnt++;
}

// void free_mem(IntObject *obj)
// {
//     if (obj == NULL) return;
//     free(obj);
// }


int main(void)
{
    printf("Mini Python Object System:\n");
    printf("\n");

    IntObject *a = new_int(101);
    TypeObject IntType = {
        .name = "int"
    };
    a->base.type = &IntType;

    IntObject *b = a;

    printf(" - a->base.refcnt = %zu\n", a->base.refcnt);
    printf(" - a->value = %ld\n", a->value);


    Py_INCREF((Object *)b);
    Py_INCREF((Object *)b);
    printf(" - a->base.refcnt = %zu\n", a->base.refcnt);
    printf(" - a->value = %ld\n", a->value);
    printf(" - a->base.type = %s\n", a->base.type->name);
    printf("\n");

    // Py_DECREF((Object *)b);
    Py_DECREF((Object *)b);
    Py_DECREF((Object *)b);
    Py_DECREF((Object *)a);


    printf(" - a->base.refcnt = %zu\n", a->base.refcnt);
//     printf(" - a->base.type = %s\n", a->base.type->name);
    printf(" - a->value = %ld\n", a->value);


    // free_mem((Object *)b);
    // free_mem((IntObject *)b);
    // free_mem((IntObject *)a);


//     printf("\n");
//     printf("Use-after-free!!!\n");
//     printf(" - a->base.refcnt = %zu\n", a->base.refcnt);
//     printf(" - a->value = %ld\n", a->value);


    return 0;
}
