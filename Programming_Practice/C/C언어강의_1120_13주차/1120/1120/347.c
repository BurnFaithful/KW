#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fp;
	char ch;

	if ((fp = fopen("basic.txt", "w")) == NULL)
	{
		printf("������ ������ �ʽ��ϴ�.\n");
		exit(1);
	}

	printf("���� �ϳ��� �Է��ϼ���.\n");
	ch = getchar();

	while (ch != 'q')
	{
		fputc(ch, fp);
		ch = getchar();
	}

	printf("���� �Է��� ����Ǿ����ϴ�.\n");

	return 0;
}