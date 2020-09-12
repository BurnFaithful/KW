#include <stdio.h>

void sorting(int *a, int size)
{
	int i, j, temp;

	for (i = 0; i < size; i++)
	{
		for (j = i + 1; j < size; j++)
		{
			if (a[i] < a[j])
			{
				temp = a[j];
				a[j] = a[i];
				a[i] = temp;
			}
		}
	}
}

int main()
{
	int a[] = { 10, 20, 3, 7, 4, 30, 11, 21, 8 };
	int *p = a;
	int i;
	sorting(a, 9);

	for (i = 0; i < 9; i++)
	{
		printf("%d  ", a[i]);
	}

	return 0;
}