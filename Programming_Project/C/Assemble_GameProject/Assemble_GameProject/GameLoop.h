#ifndef __GAMELOOP_H__
#define __GAMELOOP_H__
#include "stdafx.h"
#include "TitleScene.h"
#include "Stage1Scene.h"
#include "Stage2Scene.h"

static bool isDebug;

HDC hdc; // Main DC
GameImage* backBuffer;
eGameState gameState;
eSceneKind sceneKind;

GameScene* currentScene;

GameScene* titleScene;
GameScene* stage1_Scene;
GameScene* stage2_Scene;

Frame* timeMng;

int i, j;

GameLoop* NewGameLoop();

void Ctor_GameLoop();
void Dtor_GameLoop();

HRESULT GameInit();
void GameRelease();
void GameUpdate();
void GameRender();

LRESULT MainGameProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);

#endif