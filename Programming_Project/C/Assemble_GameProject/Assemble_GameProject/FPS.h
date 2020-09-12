#ifndef __FPS_H__
#define __FPS_H__
#include "stdafx.h"

Frame* NewTimeManager();

HRESULT FPSInit(Frame*);
void Tick(Frame*, float lockFPS);
void FPSRender(Frame*, HDC hdc);

#endif