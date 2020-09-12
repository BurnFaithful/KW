#include <stdio.h>

int main()
{
	int a = 10;
	int* p = &a;
	
	printf("a : %d\n", *p);

	return 0;
}