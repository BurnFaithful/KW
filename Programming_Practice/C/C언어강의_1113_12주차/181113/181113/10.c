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
	haha h1 = { "박민수", 80, 80, 80 };
	haha h2 = { "홍길동", 50, 50, 50 };
	haha h3 = { "김한별", 90, 90, 90 };
	haha h4 = { "광운이", 100, 100, 100 };

	printf("========================================================\n");
	printf("                  개인별 영업 실적 통계                 \n");
	printf("========================================================\n");

	printf(" 이름 \t 1월 \t 5월 \t 11월 \t총실적 \t 평균실적 \t \n");
	go(h1);
	go(h2);
	go(h3);
	go(h4);

	printf("========================================================\n");

	printf("========================================================\n");

	return 0;
}