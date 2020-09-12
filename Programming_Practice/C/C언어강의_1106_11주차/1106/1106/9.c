#include <stdio.h>

extern int b; // 전역변수 : 외부에서 사용할 수 있는 변수
static int z = 5; // 정적변수 : 프로그램이 끝날 때까지 메모리에 남아있는 변수

int main()
{
	int i;
	for (i = 0; i < 3; i++)
	{
		int a = 100; // 지역변수 : 블록 안에서만 살아있는 변수
		printf("%d\n", a);
		printf("%d\n", b);
		a++;
		z++;
		printf("%d\n", a);
		printf("%d\n\n\n", z);
	}

	return 0;
}