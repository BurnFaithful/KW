#include "Box.h"

Object* NewObject()
{
	Object* pObject = (Object*)malloc(sizeof(Object));

	pObject->Init = Init_Object;
	pObject->Release = Release_Object;
	pObject->Update = Update_Object;
	pObject->Render = Render_Object;
	pObject->FrameRender = FrameRender_Object;

	pObject->CollisionCheck = CollisionCheck_Object;
	pObject->Move = Move_Object;

	return pObject;
}

void Dtor_Object(Object* this)
{
}

HRESULT Init_Object(Object* this)
{
	return S_OK;
}

void Release_Object(Object* this)
{
	if (this->pImage != NULL)
		this->pImage->Release(this->pImage);

	if (this)
	{
		//free(this);
		//this = NULL;
	}
}

void Update_Object(Object* this)
{

}

void Render_Object(Object* this)
{
	this->pImage->Render_Pos_Scale(
		this->pImage, backBuffer->imageInfo->hMemDC,
		this->posX, 
		this->posY,
		0, 0,
		MAP_TILESIZE_WIDTH,
		MAP_TILESIZE_HEIGHT);
}

void FrameRender_Object(Object* this)
{
	this->pImage->FrameRender_Pos(
		this->pImage, backBuffer->imageInfo->hMemDC,
		this->posX, this->posY);
}

void Move_Object(Object* this)
{
	if (this->moveDir == UP)
	{
		this->posY -= MAP_TILESIZE_HEIGHT;
		this->tileY--;
	}
	else if (this->moveDir == DOWN)
	{
		this->posY += MAP_TILESIZE_HEIGHT;
		this->tileY++;
	}
	else if (this->moveDir == LEFT)
	{
		this->posX -= MAP_TILESIZE_WIDTH;
		this->tileX--;
	}
	else if (this->moveDir == RIGHT)
	{
		this->posX += MAP_TILESIZE_WIDTH;
		this->tileX++;
	}
}

int CollisionCheck_Object(Object* this, Tile* checkTile, eDirection dir)
{
	this->moveDir = dir;

	if (checkTile->tileAttribute == BLOCK ||
		checkTile->tileAttribute == BOX)
	{
		return BLOCK;
	}
	else if (checkTile->tileAttribute == HOLE)
	{
		return HOLE;
	}

	return ROAD;
}

