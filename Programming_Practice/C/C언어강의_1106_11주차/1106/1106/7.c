// ����������(�̸�,����,����,���� ��)
//ö��,90,90,90
//����.50,50,50
//����,80,80,80
//����,100,100,100
//�迭�� �̿��Ͽ� �Է��ϰ� ������ ����� ���Ͽ���

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
	char name[][8] = { "ö��","����","����","����" };
	int kor[4] = { 90,50,80,100 };
	int mat[4] = { 90,50,80,100 };
	int eng[4] = { 90,50,80,100 };

	printf("=============================================\n");
	printf("            ��   ��  ǥ  \n");
	printf("=============================================\n");
	printf(" �̸�  \t���� \t���� \t���� \t���� \t���\n");

	func(name, kor, mat, eng, 4);

	return 0;
}







