#include <stdio.h>

extern int b; // �������� : �ܺο��� ����� �� �ִ� ����
static int z = 5; // �������� : ���α׷��� ���� ������ �޸𸮿� �����ִ� ����

int main()
{
	int i;
	for (i = 0; i < 3; i++)
	{
		int a = 100; // �������� : ��� �ȿ����� ����ִ� ����
		printf("%d\n", a);
		printf("%d\n", b);
		a++;
		z++;
		printf("%d\n", a);
		printf("%d\n\n\n", z);
	}

	return 0;
}