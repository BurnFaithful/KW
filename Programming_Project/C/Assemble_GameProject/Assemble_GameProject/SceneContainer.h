//#pragma once
#ifndef __SCENECONTAINER_H__
#define __SCENECONTAINER_H__
#include "stdafx.h"

GameScene* curScene;
GameScene* sceneArr[Scene_Num];

void InitScene();
void ChangeScene(eSceneKind _sceneKind);

#endif
