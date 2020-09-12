#include <stdio.h>

int SumArray(int* pA, int size)
{
	int result = 0, i;
	for (i = 0; i < size; i++)
		result += (*pA)++;

	return result;
}

int main()
{
	int a[] = { 10, 5, 15, 25, 7 };
	int sum;
	sum = SumArray(a, 5);
	printf("배열의 합 : %d\n", sum);

	return 0;
}