#ifndef __STAGE1SCENE_H__
#define __STAGE1SCENE_H__
#include "stdafx.h"
#include "Sound.h"
#include "TileMap.h"
#include "Player.h"
#include "Box.h"

#define BOX_NUM_STAGE1 4
#define BASKET_NUM_STAGE1 1

Sound* soundMng;

GameScene* NewStage1Scene();

void Ctor_Stage1Scene();
void Dtor_Stage1Scene();

HRESULT Init_Stage1Scene();
void Release_Stage1Scene();
void Update_Stage1Scene();
void Render_Stage1Scene();

#endif