#include <stdio.h>

int main()
{
	int num = 10;
	int* pNum = &num;
	
	printf("정수형 변수 num의 값 : %d\n", (*pNum));
	printf("정수형 변수 num의 값 : %d\n", num);
	printf("정수형 변수 num의 주소 : %p\n", &num);
	printf("정수형 변수 num의 주소 : %p\n", pNum);
	return 0;
}