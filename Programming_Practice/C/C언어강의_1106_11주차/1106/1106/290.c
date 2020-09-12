#include <stdio.h>

int main()
{
	int a[] = { 5, 10, 15, 20, 25 };
	int *p = a;
	int i;

	for (i = 0; i < 5; i++)
	{
		printf("*(p+%d) + %d = %dÀÌ´Ù.\n", i, i, *(p + i) + i);
	}

	return 0;
}