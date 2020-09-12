#include <stdio.h>
#include <stdlib.h>

int main()
{
	for (int i = 1; i <= 9; i++)
	{
		for (int j = 2; j <= 9; j++)
		{
			printf("%d * %d = %d\t", j, i, j * i);
		}
		printf("\n");
	}

	system("pause");

	return 0;
}