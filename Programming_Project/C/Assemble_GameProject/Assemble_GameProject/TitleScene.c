#include "TitleScene.h"

GameScene* NewTitleScene()
{
	GameScene* pScene = (GameScene*)malloc(sizeof(GameScene));

	//pScene->Ctor = Ctor_TitleScene;
	//pScene->Dtor = Dtor_TitleScene;
	pScene->Init = Init_TitleScene;
	pScene->Release = Release_TitleScene;
	pScene->Update = Update_TitleScene;
	pScene->Render = Render_TitleScene;

	return pScene;
}

void Ctor_TitleScene()
{
}

void Dtor_TitleScene()
{
}

HRESULT Init_TitleScene()
{
	titleBG = NewImage();
	titleText = NewImage();

	titleBG->Init_Scale(
		titleBG, 
		_T("image/titleBG.bmp"), 
		WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT);
	titleText->Init_Scale_Pos_Trans(
		titleText, 
		_T("image/titleText.bmp"),
		0, 0,
		WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT,
		true, MAGENTA);

	blinkGauge = 0;
	blinkGauge = false;

	return S_OK;
}

void Release_TitleScene()
{
	titleBG->Release(titleBG);
	titleText->Release(titleText);
}

void Update_TitleScene()
{
	if (GetKeyDown('S'))
	{
		gameState = Proceed;
		currentScene->Release();
		sceneKind = Room_1;
		currentScene = stage1_Scene;
		currentScene->Init();
	}

	if (blinkGauge <= 0)
	{
		blinkReverse = true; // true가 상승, false가 감소
		blinkGauge = 0;
	}
	else if (blinkGauge >= 255)
	{
		blinkReverse = false;
		blinkGauge = 255;
	}

	if (blinkReverse)
		blinkGauge += BLINKSPEED;
	else
		blinkGauge -= BLINKSPEED;
}

void Render_TitleScene()
{
	titleBG->Render_Pos(titleBG, backBuffer->imageInfo->hMemDC,
		titleBG->imageInfo->x, titleBG->imageInfo->y);

	titleText->AlphaRender_Pos(titleText, backBuffer->imageInfo->hMemDC,
		titleText->imageInfo->x, titleText->imageInfo->y,
		blinkGauge);
}