#include <stdio.h>

struct haha
{
	char name[10];
	int janResult;
	int mayResult;
	int novemberResult;
};
typedef struct haha haha;

void go(haha a)
{
	printf("%s \t %3d \t %3d \t %3d \t\n", a.name, a.janResult, a.mayResult, a.novemberResult);
}

int main()
{
	//int i, j;
	haha h1 = { "�ڹμ�", 80, 80, 80 };
	haha h2 = { "ȫ�浿", 50, 50, 50 };
	haha h3 = { "���Ѻ�", 90, 90, 90 };
	haha h4 = { "������", 100, 100, 100 };

	printf("========================================================\n");
	printf("                  ���κ� ���� ���� ���                 \n");
	printf("========================================================\n");

	printf(" �̸� \t 1�� \t 5�� \t 11�� \t�ѽ��� \t ��ս��� \t \n");
	go(h1);
	go(h2);
	go(h3);
	go(h4);

	printf("========================================================\n");

	printf("========================================================\n");

	return 0;
}