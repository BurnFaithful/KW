#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int Add(int _x, int _y)
{
	return _x + _y;
}

int Sub(int _x, int _y)
{
	return _x - _y;
}

int Mul(int _x, int _y)
{
	return _x * _y;
}

int Divide(int _x, int _y)
{
	return _x / _y;
}

int Mod(int _x, int _y)
{
	return _x % _y;
}

int main()
{
	int num, largerNum;

	while (1)
	{
		printf("ū ���� ���� �� ������ �� ���� �Է� > ");
		scanf_s("%d %d", &largerNum, &num);
		if (largerNum >= num)
		{
			printf("=====================================\n");
			printf("���� ��� : %d + %d = %d\n", largerNum, num, Add(largerNum, num));
			printf("���� ��� : %d - %d = %d\n", largerNum, num, Sub(largerNum, num));
			printf("���� ��� : %d * %d = %d\n", largerNum, num, Mul(largerNum, num));
			printf("������ ��� : %d / %d = %d\n", largerNum, num, Divide(largerNum, num));
			printf("���������� ��� : %d %% %d = %d\n", largerNum, num, Mod(largerNum, num));
			if (_getch()) system("cls");
		}
		else
		{
			printf("���� �Է��� ���� ū ������ �մϴ�.\n");
		}
	}

	return 0;
}