#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char* printStr = "";
	
	char inputStr[256];

	printStr = fgets(inputStr, sizeof(inputStr), stdin);
	printf("%s\n", printStr);

	//printf("%c\n", inputStr[0]);

	return 0;
}