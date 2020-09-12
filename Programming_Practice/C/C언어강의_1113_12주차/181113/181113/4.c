#include <stdio.h>

void Swap(int* a, int* b)
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

int main()
{
	int num_1, num_2;

	printf("두 수를 입력 > ");
	scanf_s("%d %d", &num_1, &num_2);

	printf("함수 호출 전 : num_1 : %d, num_2 : %d\n", num_1, num_2);
	Swap(&num_1, &num_2);
	printf("함수 호출 후 : num_1 : %d, num_2 : %d\n", num_1, num_2);

	return 0;
}