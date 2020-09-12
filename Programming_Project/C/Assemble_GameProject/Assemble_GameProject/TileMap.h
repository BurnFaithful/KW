#ifndef __TILEMAP_H__
#define __TILEMAP_H__
#include "stdafx.h"

Tile* tileMap[MAP_TILE_ROWNUM][MAP_TILE_COLNUM];

int attributeArr[MAP_TILE_ROWNUM][MAP_TILE_COLNUM];

Object** box;
Object** basket;
GameImage* stepImage;
GameImage* numberImage[STEP_MAX_DIGIT];
GameImage* clearImage;

int boxCount;
int basketCount;
int stepRealCount, stepCalcCount;
int stepDigitNum[STEP_MAX_DIGIT];
int resultCount;

void SetMapTile(Tile* tile, int tileAttribte);
void RenderMapTile(Tile* tile);

void ResetMap();

#endif