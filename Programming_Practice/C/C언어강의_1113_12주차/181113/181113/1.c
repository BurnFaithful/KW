#include <stdio.h>

int main()
{
	int i, j;
	char name[][10] = { "�ڹμ�", "ȫ�浿", "���Ѻ�", "������" };
	//int janResult[4] = { 180, 50, 90, 100 };
	//int mayResult[4] = { 80, 150, 90, 100 };
	//int novemberResult[4] = { 80, 50, 190, 100 };
	int result[4][3] = { {180, 80, 80}, {50, 150, 50}, {90, 90, 190}, {100, 100, 100} }; // row : �ο��� ����, column : ��
	int total = 0;
	int monthTotal[3] = { 0, };
	double avg = 0.;

	printf("========================================================\n");
	printf("                  ���κ� ���� ���� ���                 \n");
	printf("========================================================\n");

	printf(" �̸� \t 1�� \t 5�� \t 11�� \t�ѽ��� \t ��ս��� \t \n");
	
	//for (i = 0; i < 4; i++)
	//{
	//	printf("%s \t\t %3d \t\t %3d \t\t %3d \t\t \n", name[i], janResult[i], mayResult[i], novemberResult[i]);
	//}
	for (i = 0; i < 4; i++)
	{
		total = 0;
		printf("%s \t", name[i]);

		for (j = 0; j < 3; j++)
		{
			total += result[i][j];
			printf(" %3d \t", result[i][j]);
		}
		avg = total / 3.;
		printf("%5d \t %7.2lf \t\n", total, avg);
		//printf("\n");
	}

	// �� �Ѱ� ���
	for (i = 0; i < 3; i++)
		for (j = 0; j < 4; j++)
			monthTotal[i] += result[j][i];

	printf("========================================================\n");
	printf("���Ѱ� ");
	for (i = 0; i < 3; i++)
	{
		printf("%5d \t", monthTotal[i]);
	}
	printf("\n");
	printf("========================================================\n");

	return 0;
}