#include "TileMap.h"

void SetMapTile(Tile* tile, int tileAttribute)
{

}

void RenderMapTile(Tile* tile)
{

}

void ResetMap()
{
	boxCount = 0;
	basketCount = 0;
	stepRealCount = 0;
	resultCount = 0;

	for (i = 0; i < MAP_TILE_ROWNUM; i++)
	{
		for (j = 0; j < MAP_TILE_COLNUM; j++)
		{
			tileMap[i][j]->Reset(tileMap[i][j], attributeArr[i][j], j, i);
		}
	}
}