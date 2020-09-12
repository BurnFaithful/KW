#include <stdio.h>

int main()
{
	int i, j;
	char name[][10] = { "박민수", "홍길동", "김한별", "광운이" };
	//int janResult[4] = { 180, 50, 90, 100 };
	//int mayResult[4] = { 80, 150, 90, 100 };
	//int novemberResult[4] = { 80, 50, 190, 100 };
	int result[4][3] = { {180, 80, 80}, {50, 150, 50}, {90, 90, 190}, {100, 100, 100} }; // row : 인원별 실적, column : 월
	int total = 0;
	int monthTotal[3] = { 0, };
	double avg = 0.;

	printf("========================================================\n");
	printf("                  개인별 영업 실적 통계                 \n");
	printf("========================================================\n");

	printf(" 이름 \t 1월 \t 5월 \t 11월 \t총실적 \t 평균실적 \t \n");
	
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

	// 월 총계 계산
	for (i = 0; i < 3; i++)
		for (j = 0; j < 4; j++)
			monthTotal[i] += result[j][i];

	printf("========================================================\n");
	printf("월총계 ");
	for (i = 0; i < 3; i++)
	{
		printf("%5d \t", monthTotal[i]);
	}
	printf("\n");
	printf("========================================================\n");

	return 0;
}