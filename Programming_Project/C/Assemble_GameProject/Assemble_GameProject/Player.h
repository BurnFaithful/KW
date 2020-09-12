#ifndef __PLAYER_H__
#define __PLAYER_H__
#include "stdafx.h"

Actor* player;

Actor* NewPlayer();
void Dtor_Player(Actor*);

HRESULT Init_Player(Actor*, int _x, int _y);
void Release_Player(Actor*);
void Update_Player(Actor*);
void Render_Player(Actor*);

void FrameAnimation_Player(Actor*);
void InputKey_Player(Actor*);

void SetPosition_Player(Actor*);
void Move_Player(Actor*);
int CollisionCheck_Player(Actor*, Tile*);

void SetStatus_Player(Actor*, int _x, int _y);

#endif
