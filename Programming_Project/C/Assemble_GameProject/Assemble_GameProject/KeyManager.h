#ifndef __KEYMANAGER_H__
#define __KEYMANAGER_H__
#include "stdafx.h"

bool keyDown[256];
bool keyUp[256];

bool GetKeyDown(int key);
bool GetKeyUp(int key);
bool GetKey(int key);

#endif

