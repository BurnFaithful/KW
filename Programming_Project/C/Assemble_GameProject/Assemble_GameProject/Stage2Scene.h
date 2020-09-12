#ifndef __STAGE2SCENE_H__
#define __STAGE2SCENE_H__
#include "stdafx.h"
#include "TileMap.h"
#include "Player.h"
#include "Box.h"

#define BOX_NUM_STAGE2 6
#define BASKET_NUM_STAGE2 1

GameScene* NewStage2Scene();

void Ctor_Stage2Scene();
void Dtor_Stage2Scene();

HRESULT Init_Stage2Scene();
void Release_Stage2Scene();
void Update_Stage2Scene();
void Render_Stage2Scene();

#endif