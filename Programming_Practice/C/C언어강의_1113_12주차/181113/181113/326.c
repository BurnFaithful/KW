#include <stdio.h>

struct ThreeDime
{
	double x;
	double y;
	double z;
};

typedef struct ThreeDime ThreeDime;

int main()
{
	ThreeDime A1 = { 3, 1, 8 };

	ThreeDime* pA1 = &A1;

	printf("3차원 점 A1의 x : %.2lf, y : %.2lf, z : %.2lf이다.\n", pA1->x, pA1->y, pA1->z);

	return 0;
}