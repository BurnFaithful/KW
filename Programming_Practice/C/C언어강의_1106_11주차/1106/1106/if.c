#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main()
{
	int i = 0, num;

	//for (i = 0; i < 5; ++i)
	//{
	while (1)
	{
		printf("정수 하나 입력 > ");
		scanf_s("%d", &num);

		if (num % 2 == 0)
			printf("입력한 수는 짝수입니다.\n");
		else
			printf("입력한 수는 홀수입니다.\n");

		//Sleep(1000);
		_getch();
		system("cls");
	}
	//}

	return 0;
}