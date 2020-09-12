#include "KeyManager.h"

//0x0000 (0) : ������ ���� �� ����, ȣ�� ���������� �������� �ʴ� ����
//0x0001 (1) : ������ ���� �� �ְ�, ȣ�� �������� �������� ���� ����
//0x8000 : ������ ���� �� ����, ȣ�� �������� �����ִ� ����
//0x8001 : ������ ���� �� �ְ�, ȣ�� ���������� �����ִ� ����

bool GetKeyDown(int key)
{
	if (GetAsyncKeyState(key) & 0x8000)
	{
		if (keyDown[key] == false)
		{
			keyDown[key] = true;
			return true;
		}
	}
	else keyDown[key] = false;

	return false;
}

bool GetKeyUp(int key)
{
	if (GetAsyncKeyState(key) & 0x8000)
	{
		keyUp[key] = true;
	}
	else
	{
		if (keyUp[key] == true)
		{
			keyUp[key] = false;
			return true;
		}
	}

	return false;
}

bool GetKey(int key)
{
	if (GetAsyncKeyState(key) & 0x8000) return true;
	
	return false;
}