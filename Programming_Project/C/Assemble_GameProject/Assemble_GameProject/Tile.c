#include "Tile.h"

Tile* NewTile()
{
	Tile* pTile = (Tile*)malloc(sizeof(Tile));

	pTile->Init = Init_Tile;
	pTile->Release = Release_Tile;
	pTile->Update = Update_Tile;
	pTile->Render = Render_Tile;

	pTile->Reset = Reset_Tile;

	return pTile;
}

HRESULT Init_Tile(Tile* this, int tileAttribute, int _tileX, int _tileY)
{
	this->width = MAP_TILESIZE_WIDTH;
	this->height = MAP_TILESIZE_HEIGHT;
	this->tileX = _tileX;
	this->tileY = _tileY;
	this->posX = this->tileX * this->width;
	this->posY = this->tileY * this->height;
	this->isExistBox = false;
	this->pImage = NULL;
	this->pBox = NULL;
	this->pBasket = NULL;
	this->tileAttribute = tileAttribute;

	switch (this->tileAttribute)
	{
	case BLOCK:
		this->pImage = NewImage();
		this->pImage->Init_Scale_Pos(this->pImage,
			_T("image/tile_brick.bmp"),
			this->posX,
			this->posY,
			this->width,
			this->height
		);
		break;
	case ROAD:
		this->pImage = NewImage();
		this->pImage->Init_Scale_Pos(this->pImage,
			_T("image/tile_sand.bmp"),
			this->posX,
			this->posY,
			this->width,
			this->height
		);
		break;
	case HOLE:
		basket[basketCount]->tileX = this->tileX;
		basket[basketCount]->tileY = this->tileY;
		basket[basketCount]->posX = MAP_TILESIZE_WIDTH * basket[basketCount]->tileX;
		basket[basketCount]->posY = MAP_TILESIZE_HEIGHT * basket[basketCount]->tileY;
		basket[basketCount]->width = MAP_TILESIZE_WIDTH;
		basket[basketCount]->height = MAP_TILESIZE_HEIGHT;
		basket[basketCount]->moveDir = IDLE;
		basket[basketCount]->isAssignment = true;
		basket[basketCount]->pImage = NewImage();

		basket[basketCount]->pImage->Init_Frame_Pos(
			basket[basketCount]->pImage,
			_T("image/basket.bmp"),
			basket[basketCount]->posX,
			basket[basketCount]->posY,
			basket[basketCount]->width * BASKET_FRAME_X,
			basket[basketCount]->height,
			BASKET_FRAME_X, BASKET_FRAME_Y,
			true, MAGENTA);

		this->pBasket = basket[basketCount];
		basketCount++;
		break;
	case BOX:
		this->pImage = NewImage();
		this->pImage->Init_Scale_Pos(
			this->pImage,
			_T("image/tile_sand.bmp"),
			this->posX,
			this->posY,
			this->width,
			this->height
		);
		this->isExistBox = true;
		
		box[boxCount]->tileX = this->tileX;
		box[boxCount]->tileY = this->tileY;
		box[boxCount]->posX = MAP_TILESIZE_WIDTH * box[boxCount]->tileX;
		box[boxCount]->posY = MAP_TILESIZE_HEIGHT * box[boxCount]->tileY;
		box[boxCount]->moveDir = IDLE;
		box[boxCount]->isAssignment = false;
		box[boxCount]->pImage = NewImage();

		box[boxCount]->pImage->Init_Scale_Pos_Trans(
			box[boxCount]->pImage,
			_T("image/apple.bmp"),
			box[boxCount]->posX, box[boxCount]->posY,
			MAP_TILESIZE_WIDTH, MAP_TILESIZE_HEIGHT,
			true, MAGENTA);

		this->pBox = box[boxCount];
		boxCount++;
		break;
	case PLAYER:
		this->pImage = NewImage();
		this->pImage->Init_Scale_Pos(
			this->pImage,
			_T("image/tile_sand.bmp"),
			this->posX,
			this->posY,
			this->width,
			this->height
		);

		player->Init(player, this->tileX, this->tileY);
		break;
	}

	return S_OK;
}

void Release_Tile(Tile* this)
{
	if (this->pImage != NULL)
		this->pImage->Release(this->pImage);

	//if (this)
	//{
	//	free(this);
	//	this = NULL;
	//}
}

void Update_Tile(Tile* this)
{

}

void Render_Tile(Tile* this)
{
	if (this->pImage != NULL)
	{
		this->pImage->Render_Pos(this->pImage,
			backBuffer->imageInfo->hMemDC,
			this->posX, this->posY);
	}
}

void Reset_Tile(Tile* this, int tileAttribute, int _tileX, int _tileY)
{
	this->width = MAP_TILESIZE_WIDTH;
	this->height = MAP_TILESIZE_HEIGHT;
	this->tileX = _tileX;
	this->tileY = _tileY;
	this->posX = this->tileX * this->width;
	this->posY = this->tileY * this->height;
	this->isExistBox = false;
	//this->pImage = NULL;
	this->pBox = NULL;
	this->pBasket = NULL;
	this->tileAttribute = tileAttribute;

	switch (this->tileAttribute)
	{
	case HOLE:
		basket[basketCount]->tileX = this->tileX;
		basket[basketCount]->tileY = this->tileY;
		basket[basketCount]->posX = MAP_TILESIZE_WIDTH * basket[basketCount]->tileX;
		basket[basketCount]->posY = MAP_TILESIZE_HEIGHT * basket[basketCount]->tileY;
		basket[basketCount]->width = MAP_TILESIZE_WIDTH;
		basket[basketCount]->height = MAP_TILESIZE_HEIGHT;
		basket[basketCount]->moveDir = IDLE;
		basket[basketCount]->isAssignment = true;

		this->pBasket = basket[basketCount];
		basketCount++;
		break;
	case BOX:
		this->isExistBox = true;

		box[boxCount]->tileX = this->tileX;
		box[boxCount]->tileY = this->tileY;
		box[boxCount]->posX = MAP_TILESIZE_WIDTH * box[boxCount]->tileX;
		box[boxCount]->posY = MAP_TILESIZE_HEIGHT * box[boxCount]->tileY;
		box[boxCount]->moveDir = IDLE;
		box[boxCount]->isAssignment = false;

		this->pBox = box[boxCount];
		boxCount++;
		break;
	case PLAYER:
		player->SetStatus(player, this->tileX, this->tileY);
		break;
	}
}