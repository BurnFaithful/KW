#include "Stage2Scene.h"

GameScene* NewStage2Scene()
{
	GameScene* pScene = (GameScene*)malloc(sizeof(GameScene));

	pScene->Init = Init_Stage2Scene;
	pScene->Release = Release_Stage2Scene;
	pScene->Update = Update_Stage2Scene;
	pScene->Render = Render_Stage2Scene;

	return pScene;
}

void Ctor_Stage2Scene()
{
}

void Dtor_Stage2Scene()
{
}

HRESULT Init_Stage2Scene()
{
	int tempAttributeArr[MAP_TILE_ROWNUM][MAP_TILE_COLNUM] =
	{
		{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 },
	{ 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0 },
	{ 0, 1, 1, 1, 1, 0, 1, 3, 1, 1, 1, 3, 1, 1, 0, 0 },
	{ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0 },
	{ 0, 0, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0 },
	{ 0, 0, 1, 4, 3, 1, 1, 0, 1, 3, 1, 3, 1, 1, 0, 0 },
	{ 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0 },
	{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
	};

	PlaySound(_T(BGM), NULL, SND_ASYNC | SND_LOOP);

	player = NewPlayer();

	boxCount = 0;
	basketCount = 0;
	stepRealCount = 0;
	resultCount = 0;

	box = (Object**)malloc(sizeof(Object*) * BOX_NUM_STAGE2);
	basket = (Object**)malloc(sizeof(Object*) * BASKET_NUM_STAGE1);
	for (i = 0; i < BOX_NUM_STAGE2; i++)
		box[i] = NewObject();
	for (i = 0; i < BASKET_NUM_STAGE2; i++)
		basket[i] = NewObject();

	for (i = 0; i < MAP_TILE_ROWNUM; i++)
	{
		for (j = 0; j < MAP_TILE_COLNUM; j++)
		{
			attributeArr[i][j] = tempAttributeArr[i][j];
			tileMap[i][j] = NewTile();
			tileMap[i][j]->Init(tileMap[i][j], attributeArr[i][j], j, i);
		}
	}

	stepImage = NewImage();
	stepImage->Init_Scale_Pos_Trans(stepImage,
		_T("image/step.bmp"),
		0, 0,
		MAP_TILESIZE_WIDTH * 2, MAP_TILESIZE_HEIGHT,
		true, MAGENTA);

	for (i = 0; i < STEP_MAX_DIGIT; i++)
	{
		numberImage[i] = NewImage();
		numberImage[i]->Init_Frame(numberImage[i],
			_T("image/number.bmp"),
			MAP_TILESIZE_WIDTH * 10, MAP_TILESIZE_HEIGHT,
			10, 1,
			true, MAGENTA);
	}

	clearImage->Init_Scale_Pos_Trans(clearImage,
		_T("image/gameClear.bmp"),
		0, 0,
		WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT,
		true, MAGENTA);

	return S_OK;
}

void Release_Stage2Scene()
{
	for (i = 0; i < MAP_TILE_ROWNUM; i++)
	{
		for (j = 0; j < MAP_TILE_COLNUM; j++)
		{
			tileMap[i][j]->Release(tileMap[i][j]);
		}
	}

	for (i = 0; i < BOX_NUM_STAGE2; i++)
		box[i]->Release(box[i]);
	free(box);
	
	for (i = 0; i < BASKET_NUM_STAGE2; i++)
		basket[i]->Release(basket[i]);
	free(basket);

	player->Release(player);

	stepImage->Release(stepImage);
	for (i = 0; i < STEP_MAX_DIGIT; i++)
		numberImage[i]->Release(numberImage[i]);
	clearImage->Release(clearImage);
}

void Update_Stage2Scene()
{
	switch (gameState)
	{
	case Proceed:
		if (resultCount >= BOX_NUM_STAGE2)
		{
			gameState = Clear;
			PlaySound(_T(CLEAR_SOUND), NULL, SND_ASYNC | SND_LOOP);
		}
		
		if (GetKeyDown('A')) ResetMap();

		for (i = 0; i < BOX_NUM_STAGE2; i++)
			box[i]->Update(box[i]);

		player->Update(player);

		i = STEP_MAX_DIGIT - 1;
		stepCalcCount = stepRealCount;
		while (stepCalcCount != 0)
		{
			stepDigitNum[i] = stepCalcCount % 10;
			stepCalcCount /= 10;
			numberImage[i]->imageInfo->curFrameX = stepDigitNum[i];
			i--;
		}

		basket[0]->pImage->imageInfo->curFrameX = resultCount;
		break;
	case Clear:
		if (GetKeyDown('S')) PostQuitMessage(0);
		break;
	}
}

void Render_Stage2Scene()
{
	for (i = 0; i < MAP_TILE_ROWNUM; i++)
	{
		for (j = 0; j < MAP_TILE_COLNUM; j++)
		{
			tileMap[i][j]->Render(tileMap[i][j]);
		}
	}

	for (i = 0; i < BOX_NUM_STAGE2; i++)
	{
		if (!box[i]->isAssignment)
			box[i]->Render(box[i]);
	}

	for (i = 0; i < BASKET_NUM_STAGE2; i++)
	{
		basket[i]->FrameRender(basket[i]);
	}

	player->Render(player);

	stepImage->Render_Pos(stepImage,
		backBuffer->imageInfo->hMemDC,
		0, 0);

	for (i = 0; i < STEP_MAX_DIGIT; i++)
	{
		numberImage[i]->FrameRender_Pos(numberImage[i],
			backBuffer->imageInfo->hMemDC,
			MAP_TILESIZE_WIDTH * (2 + i),
			0);
	}

	if (gameState == Clear)
	{
		clearImage->Render(clearImage,
			backBuffer->imageInfo->hMemDC);
	}
}