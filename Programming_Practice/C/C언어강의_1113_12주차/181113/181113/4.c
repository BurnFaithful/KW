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

	printf("�� ���� �Է� > ");
	scanf_s("%d %d", &num_1, &num_2);

	printf("�Լ� ȣ�� �� : num_1 : %d, num_2 : %d\n", num_1, num_2);
	Swap(&num_1, &num_2);
	printf("�Լ� ȣ�� �� : num_1 : %d, num_2 : %d\n", num_1, num_2);

	return 0;
}