#ifndef __TILE_H__
#define __TILE_H__
#include "stdafx.h"

Tile* NewTile();

HRESULT Init_Tile(Tile* this, int tileAttribute, int _tileX, int _tileY);
void Release_Tile(Tile* this);
void Update_Tile(Tile* this);
void Render_Tile(Tile* this);

void Reset_Tile(Tile* this, int tileAttribute, int _tileX, int _tileY);

#endif
