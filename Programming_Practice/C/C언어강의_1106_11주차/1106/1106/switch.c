#include <stdio.h>
//#include <windows.h>
#include <stdlib.h>

int main()
{
	int num;

	while (1)
	{
		printf("정수 하나를 입력 > ");
		scanf_s("%d", &num);

		switch (num)
		{
		case 1:
			printf("★★★★★\n");
			break;
		case 2:
			printf("◆◆◆◆◆\n");
			break;
		case 3:
			printf("♥♥♥♥♥\n");
			break;
		case 4:
			printf("♣♣♣♣♣\n");
			break;
		case 5:
			printf("♬♬♬♬♬\n");
			break;
		default:
			system("cls");
			printf("다시 입력하세요!!\n");
			break;
		}
	}

	return 0;
}