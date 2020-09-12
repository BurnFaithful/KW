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
		printf("큰 수와 작은 수 순으로 두 수를 입력 > ");
		scanf_s("%d %d", &largerNum, &num);
		if (largerNum >= num)
		{
			printf("=====================================\n");
			printf("덧셈 결과 : %d + %d = %d\n", largerNum, num, Add(largerNum, num));
			printf("뺄셈 결과 : %d - %d = %d\n", largerNum, num, Sub(largerNum, num));
			printf("곱셈 결과 : %d * %d = %d\n", largerNum, num, Mul(largerNum, num));
			printf("나눗셈 결과 : %d / %d = %d\n", largerNum, num, Divide(largerNum, num));
			printf("나머지연산 결과 : %d %% %d = %d\n", largerNum, num, Mod(largerNum, num));
			if (_getch()) system("cls");
		}
		else
		{
			printf("먼저 입력한 수가 큰 수여야 합니다.\n");
		}
	}

	return 0;
}