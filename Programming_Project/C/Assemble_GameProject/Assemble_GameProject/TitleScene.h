#ifndef __TITLESCENE_H__
#define __TITLESCENE_H__
#include "stdafx.h"

#define BLINKSPEED 15

GameImage* titleBG;
GameImage* titleText;

int blinkGauge; // ������ ������ ���� Alpha ��
bool blinkReverse; // Fade In/Out

GameScene* NewTitleScene();

void Ctor_TitleScene();
void Dtor_TitleScene();

HRESULT Init_TitleScene();
void Release_TitleScene();
void Update_TitleScene();
void Render_TitleScene();

#endif
