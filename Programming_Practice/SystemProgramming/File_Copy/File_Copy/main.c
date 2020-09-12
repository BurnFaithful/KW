#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

void WriteFile(const char* fileName, const char* writeStr);
void ReadFile(const char* fileName);
void DecimalToBinary(int decimal);

int main()
{
	const char* fileName = "test.txt";
	const char* writeStr = "Hello, World\nFile Read\n";

	//WriteFile(fileName, writeStr);
	//ReadFile(fileName);

	DecimalToBinary(120);

	system("pause");

	return 0;
}

void WriteFile(const char* fileName, const char* writeStr)
{
	errno_t err;
	FILE* fp_write;
	if (err = fopen_s(&fp_write, fileName, "w") == 0)
	{
		fputs(writeStr, fp_write);
		printf("Write\n");
	}
	else
	{
		perror("File Write Error!");
	}

	fclose(fp_write);
}

void ReadFile(const char* fileName)
{
	errno_t err;
	FILE* fp_read;
	char str[20];
	if (err = fopen_s(&fp_read, fileName, "r") == 0)
	{
		while (fgets(str, sizeof(str), fp_read) != NULL)
		{
			printf("%s\n", str);
		}
	}
	else
	{
		perror("File Read Error");
	}
	fclose(fp_read);
}

void DecimalToBinary(int decimal)
{
	if (decimal > 0)
	{
		DecimalToBinary(decimal / 2);

		printf("%d", decimal % 2);
	}
}
