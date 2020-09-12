#include <stdio.h>

int main()
{
	enum {yellow, red, blue, green} color;

	printf("원하는 색을 입력하세요.\n");
	printf("0번 : 노란색, 1번 : 빨간색\n");
	printf("2번 : 파란색, 3번 : 초록색\n");
	scanf_s("%d", &color);

	if (color == yellow) printf("노란색입니다.\n");
	else if (color == red) printf("빨간색입니다.\n");
	else if (color == blue) printf("파란색입니다.\n");
	else if (color == green) printf("초록색입니다.\n");

	return 0;
}