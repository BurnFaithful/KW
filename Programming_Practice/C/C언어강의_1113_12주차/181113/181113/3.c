#include <stdio.h>

int main()
{
	int num = 10;
	int* pNum = &num;
	
	printf("������ ���� num�� �� : %d\n", (*pNum));
	printf("������ ���� num�� �� : %d\n", num);
	printf("������ ���� num�� �ּ� : %p\n", &num);
	printf("������ ���� num�� �ּ� : %p\n", pNum);
	return 0;
}