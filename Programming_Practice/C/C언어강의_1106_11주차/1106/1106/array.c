#include <stdio.h>

int main()
{
	int i, total = 0;
	double avg = 0.; // 평균

	char name[][10] = { "철수", "영희", "민희", "광운" }; // 이름을 배열로 저장. 행은 생략 가능.
	int kor[4] = { 90, 50, 80, 100 };
	int eng[4] = { 90, 50, 80, 100 };
	int mat[4] = { 90, 50, 80, 100 };

	printf("==============================================\n");
	printf("             성       적       표     \n");
	printf("이름\t국어\t영어\t수학\t총점\t평균\n"); // \t는 수평 탭

	for (i = 0; i < 4; ++i) // 배열 값을 for문을 통해 반복하여 사용
	{
		total = kor[i] + eng[i] + mat[i]; // 국어, 영어, 수학의 총점을 계산.
		avg = total / 3.; // avg는 double형이기 때문에 double 값으로 나눔.
		printf("%s   \t%3d   \t%3d   \t%3d   \t%3d   \t%5.1lf\n", name[i], kor[i], eng[i], mat[i], total, avg); // 2차원 배열 name의 행 인덱스로 문자열을 가져올 수 있음.
	}
	printf("==============================================\n");

	return 0;
}