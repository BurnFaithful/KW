#include <stdio.h>

int main()
{
	int a = 100;
	int *pa = &a;

	printf("a : %d\n", a);
	printf("&a : %p\n", &a);
	printf("*pa : %d\n", *pa);
	printf("pa : %p\n", pa);
	printf("&pa : %p\n", &pa);

	return 0;
}