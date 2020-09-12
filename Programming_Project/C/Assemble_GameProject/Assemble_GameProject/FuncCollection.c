#include "FuncCollection.h"

void Swap(Tile* _x1, Tile* _x2)
{
	Tile tempTile;
	
	tempTile = *_x1;
	*_x1 = *_x2;
	*_x2 = tempTile;
}