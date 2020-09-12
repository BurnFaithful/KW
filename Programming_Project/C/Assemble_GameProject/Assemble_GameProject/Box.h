#ifndef __BOX_H__
#define __BOX_H__
#include "stdafx.h"

Object* NewObject();
void Dtor_Object(Object*);

HRESULT Init_Object(Object*);
void Release_Object(Object*);
void Update_Object(Object*);
void Render_Object(Object*);
void FrameRender_Object(Object*);

void Move_Object(Object*);
int CollisionCheck_Object(Object* this, Tile* checkTile, eDirection dir);

#endif