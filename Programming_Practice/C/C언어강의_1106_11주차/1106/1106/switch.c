#include <stdio.h>
//#include <windows.h>
#include <stdlib.h>

int main()
{
	int num;

	while (1)
	{
		printf("���� �ϳ��� �Է� > ");
		scanf_s("%d", &num);

		switch (num)
		{
		case 1:
			printf("�ڡڡڡڡ�\n");
			break;
		case 2:
			printf("�ߡߡߡߡ�\n");
			break;
		case 3:
			printf("����������\n");
			break;
		case 4:
			printf("����������\n");
			break;
		case 5:
			printf("�ݢݢݢݢ�\n");
			break;
		default:
			system("cls");
			printf("�ٽ� �Է��ϼ���!!\n");
			break;
		}
	}

	return 0;
}