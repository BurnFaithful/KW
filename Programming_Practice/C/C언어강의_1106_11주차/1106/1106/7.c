// 성적데이터(이름,국어,영어,수학 순)
//철수,90,90,90
//영희.50,50,50
//민희,80,80,80
//광운,100,100,100
//배열을 이용하여 입력하고 총점과 평균을 구하여라

#include <stdio.h>

void func(char name[][8], int kor[], int mat[], int eng[], int size) 
{
	int i, tot;
	double avg;

	for (i = 0; i < 4; i++) 
	{
		tot = kor[i] + mat[i] + eng[i];
		avg = tot / 3.;
		printf(" %s \t%d  \t%d  \t%d  \t%d  \t%.1lf\n",
			name[i], kor[i], mat[i], eng[i], tot, avg);
	}
	printf("=============================================\n");
}

int main() 
{
	char name[][8] = { "철수","영희","민희","광운" };
	int kor[4] = { 90,50,80,100 };
	int mat[4] = { 90,50,80,100 };
	int eng[4] = { 90,50,80,100 };

	printf("=============================================\n");
	printf("            성   적  표  \n");
	printf("=============================================\n");
	printf(" 이름  \t국어 \t영어 \t수학 \t총점 \t평균\n");

	func(name, kor, mat, eng, 4);

	return 0;
}







