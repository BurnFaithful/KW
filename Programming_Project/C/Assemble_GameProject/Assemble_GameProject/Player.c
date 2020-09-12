#include "Player.h"

Actor* NewPlayer()
{
	Actor* pActor = (Actor*)malloc(sizeof(Actor));

	pActor->Init = Init_Player;
	pActor->Release = Release_Player;
	pActor->Update = Update_Player;
	pActor->Render = Render_Player;

	pActor->CollisionCheck = CollisionCheck_Player;

	pActor->SetPosition = SetPosition_Player;
	pActor->Move = Move_Player;
	pActor->SetStatus = SetStatus_Player;

	return pActor;
}

void Dtor_Player(Actor* this)
{
}

HRESULT Init_Player(Actor* this, int _x, int _y)
{
	this->SetStatus(this, _x, _y);

	this->pImage = NewImage();
	this->pImage->Init_Frame_Pos(this->pImage,
		_T("image/player.bmp"),
		this->posX, this->posY,
		this->width * PLAYER_FRAME_X, 
		this->height * PLAYER_FRAME_Y,
		PLAYER_FRAME_X, PLAYER_FRAME_Y,
		true, MAGENTA);

	return S_OK;
}

void Release_Player(Actor* this)
{
	if (this->pImage != NULL)
		this->pImage->Release(this->pImage);

	//if (this)
	//{
	//	free(this);
	//	this = NULL;
	//}
}

void Update_Player(Actor* this)
{
	FrameAnimation_Player(this); // Animation
	InputKey_Player(this); // Key Input
	Move_Player(this); // Move
}

void Render_Player(Actor* this)
{
 	this->pImage->FrameRender_Pos(this->pImage, 
		backBuffer->imageInfo->hMemDC,
		this->posX, this->posY);
}

void FrameAnimation_Player(Actor* this)
{
	// Animation ******************************************
	this->deltaTime += timeMng->elapsedTime;

	if (this->deltaTime > this->frameInterval)
	{
		this->pImage->imageInfo->curFrameX++;
		if (this->pImage->imageInfo->curFrameX > this->pImage->imageInfo->maxFrameX)
		{
			this->pImage->imageInfo->curFrameX = 0;
		}
		this->deltaTime = 0.f;
	}
	// Animation ******************************************
}

void InputKey_Player(Actor* this)
{
	// Input Key ******************************************
	if (!this->isMoving && GetKeyDown(VK_UP))
	{
		if (this->tileY > 0)
		{
			this->moveDir = UP;
			this->pImage->imageInfo->curFrameY = 0;
		}
	}
	else if (!this->isMoving && GetKeyDown(VK_DOWN))
	{
		if (this->tileY < MAP_TILE_ROWNUM - 1)
		{
			this->moveDir = DOWN;
			this->pImage->imageInfo->curFrameY = 1;
		}

	}
	else if (!this->isMoving && GetKeyDown(VK_LEFT))
	{
		if (this->tileX > 0)
		{
			this->moveDir = LEFT;
			this->pImage->imageInfo->curFrameY = 2;
		}
	}
	else if (!this->isMoving && GetKeyDown(VK_RIGHT))
	{
		if (this->tileX < MAP_TILE_COLNUM - 1)
		{
			this->moveDir = RIGHT;
			this->pImage->imageInfo->curFrameY = 3;
		}
	}

	if (GetKeyUp(VK_LEFT) ||
		GetKeyUp(VK_RIGHT) ||
		GetKeyUp(VK_UP) ||
		GetKeyUp(VK_DOWN))
	{
		this->moveDir = IDLE;
	}

	if (GetKeyDown('R')) // 리셋 버튼
	{
		if (currentScene != titleScene)
		{
			// Reset
		}
	}
	// Input Key ******************************************
}

void SetPosition_Player(Actor* this)
{
	switch (this->moveDir)
	{
	case UP:
		stepRealCount++;
		this->posY -= MAP_TILESIZE_HEIGHT;
		this->tileY--;
		this->moveDir = IDLE;
		break;
	case DOWN:
		stepRealCount++;
		this->posY += MAP_TILESIZE_HEIGHT;
		this->tileY++;
		this->moveDir = IDLE;
		break;
	case LEFT:
		stepRealCount++;
		this->posX -= MAP_TILESIZE_HEIGHT;
		this->tileX--;
		this->moveDir = IDLE;
		break;
	case RIGHT:
		stepRealCount++;
		this->posX += MAP_TILESIZE_HEIGHT;
		this->tileX++;
		this->moveDir = IDLE;
		break;
	default:
		break;
	}
}

void Move_Player(Actor* this)
{
	int xMoveDistance = 0;
	int yMoveDistance = 0;

	switch (this->moveDir)
	{
	case UP:
		xMoveDistance = 0;
		yMoveDistance = -1;
		break;
	case DOWN:
		xMoveDistance = 0;
		yMoveDistance = 1;
		break;
	case LEFT:
		xMoveDistance = -1;
		yMoveDistance = 0;
		break;
	case RIGHT:
		xMoveDistance = 1;
		yMoveDistance = 0;
		break;
	}

	if (this->CollisionCheck(
		this,
		tileMap[this->tileY + yMoveDistance][this->tileX + xMoveDistance]) == ROAD)
	{
		this->SetPosition(this);
	}
	else if (this->CollisionCheck(
		this,
		tileMap[this->tileY + yMoveDistance][this->tileX + xMoveDistance]) == BOX)
	{
		Object* tempObj = tileMap[this->tileY + yMoveDistance][this->tileX + xMoveDistance]->pBox;

		if (tempObj->CollisionCheck(
			tempObj,
			tileMap[this->tileY + (yMoveDistance * 2)][this->tileX + (xMoveDistance * 2)],
			this->moveDir) == ROAD)
		{
			tempObj->Move(tempObj);

			this->SetPosition(this);

			Swap(tileMap[this->tileY][this->tileX],
				tileMap[this->tileY + yMoveDistance][this->tileX + xMoveDistance]);
		}
		else if (tempObj->CollisionCheck(
			tempObj,
			tileMap[this->tileY + (yMoveDistance * 2)][this->tileX + (xMoveDistance * 2)],
			this->moveDir) == HOLE)
		{
			tempObj->Move(tempObj);

			this->SetPosition(this);

			tileMap[this->tileY][this->tileX]->tileAttribute = ROAD;
			tileMap[this->tileY][this->tileX]->pBox->isAssignment = true;

			resultCount++;
		}
	}
}

int CollisionCheck_Player(Actor* this, Tile* checkTile)
{
	if (checkTile->tileAttribute == BLOCK)
	{
		return BLOCK;
	}
	else if (checkTile->tileAttribute == BOX)
	{
		return BOX;
	}

	return ROAD;
}

void SetStatus_Player(Actor* this, int _x, int _y)
{
	this->tileX = _x;
	this->tileY = _y;
	this->width = MAP_TILESIZE_WIDTH;
	this->height = MAP_TILESIZE_HEIGHT;
	this->posX = this->tileX * this->width;
	this->posY = this->tileY * this->height;
	this->deltaTime = 0.f;
	this->frameInterval = 0.15f;
	this->isMoving = false;
	this->moveDir = IDLE;
}
