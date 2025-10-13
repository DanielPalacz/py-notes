#include <stdio.h>

char surname[20];

int main(void) {
	printf("Give your name:\n");
	char name[20];
	scanf("%s", name);
	printf("Give your surname:\n");
	scanf("%s", surname);
	return 0;
}
