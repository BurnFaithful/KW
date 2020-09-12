#include "KeyManager.h"

//0x0000 (0) : 이전에 누른 적 없고, 호출 시점에서도 눌려있지 않는 상태
//0x0001 (1) : 이전에 누른 적 있고, 호출 시점에서 눌려있지 않은 상태
//0x8000 : 이전에 누른 적 없고, 호출 시점에서 눌려있는 상태
//0x8001 : 이전에 누른 적 있고, 호출 시점에서도 눌려있는 상태

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