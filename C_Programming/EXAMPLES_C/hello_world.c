#include <stdio.h>


int print_something() {
	printf("Hello World1\n");
	return 8; // echo $?  # wypisze 8
}



int main() {
    int a = print_something();
    return a;
}
