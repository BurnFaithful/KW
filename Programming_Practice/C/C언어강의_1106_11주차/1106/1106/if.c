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
		printf("���� �ϳ� �Է� > ");
		scanf_s("%d", &num);

		if (num % 2 == 0)
			printf("�Է��� ���� ¦���Դϴ�.\n");
		else
			printf("�Է��� ���� Ȧ���Դϴ�.\n");

		//Sleep(1000);
		_getch();
		system("cls");
	}
	//}

	return 0;
}