#include <stdio.h>

int main()
{
	enum {yellow, red, blue, green} color;

	printf("���ϴ� ���� �Է��ϼ���.\n");
	printf("0�� : �����, 1�� : ������\n");
	printf("2�� : �Ķ���, 3�� : �ʷϻ�\n");
	scanf_s("%d", &color);

	if (color == yellow) printf("������Դϴ�.\n");
	else if (color == red) printf("�������Դϴ�.\n");
	else if (color == blue) printf("�Ķ����Դϴ�.\n");
	else if (color == green) printf("�ʷϻ��Դϴ�.\n");

	return 0;
}