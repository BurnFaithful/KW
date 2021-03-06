// stdafx.h : 자주 사용하지만 자주 변경되지는 않는
// 표준 시스템 포함 파일 또는 프로젝트 관련 포함 파일이
// 들어 있는 포함 파일입니다.
//

//typedef unsigned long       DWORD;
//typedef int                 BOOL;
//typedef unsigned char       BYTE;
//typedef unsigned short      WORD;
//typedef int                 INT;
//typedef unsigned int        UINT;

// WCHAR : wchar_t
// ATOM : WORD == unsigned short
// BOOL : int
// LRESULT : LONG_PTR == long

//#pragma once
#ifndef __STDAFX_H__
#define __STDAFX_H__

#include "targetver.h"

#define WIN32_LEAN_AND_MEAN             // 거의 사용되지 않는 내용은 Windows 헤더에서 제외합니다.
#define _CRT_SECURE_NO_WARNINGS			// strcpy 컴파일 에러 방지
// Windows Header
#include <windows.h>

// Include Standard Header
#include <stdio.h> // 입출력
#include <stdlib.h> // 표준 라이브러리(malloc, free, ...)
#include <malloc.h>
#include <memory.h>
#include <tchar.h> // 유니코드&멀티바이트
#include <string.h> // 문자열
#include <stdbool.h> // boolean 자료형
#include <mmsystem.h> // 사운드(wav)
#include <Digitalv.h>


// Define
#define WINDOW_SIZE_WIDTH 1280
#define WINDOW_SIZE_HEIGHT 720
#define MAP_TILESIZE_WIDTH 80
#define MAP_TILESIZE_HEIGHT 80
#define MAP_TILE_COLNUM WINDOW_SIZE_WIDTH / MAP_TILESIZE_WIDTH
#define MAP_TILE_ROWNUM WINDOW_SIZE_HEIGHT / MAP_TILESIZE_HEIGHT

#define MAGENTA RGB(255, 0, 255)
#define BGM "sound/bgm.wav"
#define CLEAR_SOUND "sound/clear.wav"

#define BASKET_FRAME_X 7
#define BASKET_FRAME_Y 1
#define PLAYER_FRAME_X 8
#define PLAYER_FRAME_Y 4
#define STEP_MAX_DIGIT 3

// Console Screen
//#ifdef UNICODE
//#pragma comment(linker, "/entry:wWinMainCRTStartup /subsystem:console")
//#else
//#pragma comment(linker, "/entry:WinMainCRTStartup /subsystem:console")
//#endif

// extern
extern HINSTANCE g_hInst;
extern HWND g_hWnd;
extern POINT g_ptMouse;

// Enum
typedef enum _eGameState
{
	Proceed,
	Clear
} eGameState;
extern eGameState gameState;

typedef enum _eSceneKind
{
	Title,
	Room_1,
	Room_2,
	Room_3,
	Scene_Num
} eSceneKind;
extern eSceneKind sceneKind;

typedef enum _eTileAttribute
{
	BLOCK,
	ROAD,
	HOLE,
	BOX,
	PLAYER
} eTileAttribute;

typedef enum _eDirection
{
	IDLE,
	LEFT,
	RIGHT,
	UP,
	DOWN
} eDirection;

// Structure
typedef struct tagGame
{
	HRESULT(*Init)();
	void(*Release)();
	void(*Update)();
	void(*Render)();

} GameLoop;

typedef struct tagFrame
{
	bool isHighPerformance;
	float timeScale;
	float elapsedTime;
	__int64 curTime;
	__int64 lastTime;
	__int64 periodFrequency;

	DWORD frameRate;
	DWORD fpsFrameCount;

	float fpsElapsedTime;
	float worldTime;

	HRESULT(*Init)(struct Frame*);
	void(*Tick)(struct Frame*, float lockFPS);
	void(*Render)(struct Frame*, HDC hdc);

} Frame;

typedef struct tagScene
{
	HRESULT(*Init)();
	void(*Release)();
	void(*Update)();
	void(*Render)();

} GameScene;

typedef struct tagImage
{
	DWORD id;
	HDC hMemDC;
	int x;
	int y;
	int width;
	int height;
	HBITMAP image;
	HBITMAP hOldBitmap;

	int curFrameX;
	int curFrameY;
	int maxFrameX;
	int maxFrameY;
	int frameWidth;
	int frameHeight;
} Image;

typedef struct tagGameImage
{
	LPCTSTR fileName;
	Image* imageInfo;
	BLENDFUNCTION blendFunc;
	Image* blendImageInfo;
	bool isTrans;
	COLORREF transColor;

	HRESULT(*Init_Set)(struct GameImage*, int _width, int _height);
	HRESULT(*Init_Scale)(struct GameImage*, LPCTSTR _fileName, int _width, int _height);
	HRESULT(*Init_Scale_Pos)(struct GameImage*, LPCTSTR _fileName, int _x, int _y, int _width, int _height);
	HRESULT(*Init_Scale_Pos_Trans)(struct GameImage*, LPCTSTR _fileName, int _x, int _y, int _width, int _height, bool, COLORREF);

	HRESULT(*Init_Frame)(struct GameImage*, LPCTSTR _fileName, int _width, int _height, int _frameX, int _frameY, bool, COLORREF);
	HRESULT(*Init_Frame_Pos)(struct GameImage*, LPCTSTR _fileName, int _x, int _y, int _width, int _height, int _frameX, int _frameY, bool, COLORREF);
	void(*Release)(struct GameImage*);

	void(*Render)(struct GameImage*, HDC hdc);
	void(*Render_Pos)(struct GameImage*, HDC hdc, int destX, int destY);
	void(*Render_Pos_Scale)(struct GameImage*, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight);
	void(*AlphaRender)(struct GameImage*, HDC hdc, BYTE alpha);
	void(*AlphaRender_Pos)(struct GameImage*, HDC hdc, int destX, int destY, BYTE alpha);
	void(*AlphaRender_Pos_Scale)(struct GameImage*, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight, BYTE alpha);
	void(*FrameRender_Pos)(struct GameImage*, HDC hdc, int destX, int destY);
	void(*FrameRender_Pos_Set)(struct GameImage*, HDC hdc, int destX, int destY, int curFrameX, int curFrameY);
	void(*AlphaFrameRender_Pos_Set)(struct GameImage*, HDC hdc, int destX, int destY, int curFrameX, int curFrameY, BYTE alpha);
} GameImage;

typedef struct tagObject
{
	DWORD id;
	int posX, posY;
	int tileX, tileY;
	int width;
	int height;
	GameImage* pImage;
	float deltaTime;
	eDirection moveDir;
	bool isAssignment;

	void(*Ctor)(struct Object*);
	void(*Dtor)(struct Object*);

	HRESULT(*Init)(struct Object*);
	void(*Release)(struct Object*);
	void(*Update)(struct Object*);
	void(*Render)(struct Object*);
	void(*FrameRender)(struct Object*);

	int(*CollisionCheck)(struct Object*, struct Tile* checkTile, eDirection dir);
	void(*Move)(struct Object*);

} Object;

typedef struct tagTile
{
	eTileAttribute tileAttribute;
	GameImage* pImage;
	Object* pBox;
	Object* pBasket;
	int tileX, tileY;
	int posX, posY;
	int width, height;
	bool isExistBox;

	HRESULT(*Init)(struct Tile*, int tileAttribute, int _tileX, int _tileY);
	void(*Release)(struct Tile*);
	void(*Update)(struct Tile*);
	void(*Render)(struct Tile*);

	void(*Reset)(struct Tile*, int tileAttribute, int _tileX, int _tileY);
} Tile;

typedef struct tagActor
{
	DWORD id;
	eDirection moveDir;
	int posX, posY;
	int tileX, tileY;
	int width;
	int height;
	GameImage* pImage;
	float deltaTime;
	float frameInterval;
	bool isMoving;

	HRESULT(*Init)(struct Actor*, int _x, int _y);
	void(*Release)(struct Actor*);
	void(*Update)(struct Actor*);
	void(*Render)(struct Actor*);

	int(*CollisionCheck)(struct Actor*, Tile* checkTile);
	void(*SetPosition)(struct Actor*);
	void(*Move)(struct Actor*);

	void(*SetStatus)(struct Actor*, int _x, int _y);
} Actor;

typedef struct tagSound
{
	MCI_OPEN_PARMS m_mciOpenParms;
	MCI_PLAY_PARMS m_mciPlayParms;
	DWORD m_dwDeviceID;
	MCI_OPEN_PARMS mciOpen; // File Load
	MCI_PLAY_PARMS mciPlay; // File Play
	MCI_STATUS_PARMS mciStatus; // File Status

	UINT wDeviceID;

	DWORD(*LoadWav)(HWND hWnd, LPCTSTR lpszWave);
	DWORD(*PlayWav)(HWND hWnd, LPCTSTR lpszWave);
} Sound;


// Macro
#define RELEASE(p) if(p) {p->Release(); (p)=NULL;}}

// TODO: 프로그램에 필요한 추가 헤더는 여기에서 참조합니다.
#include "FuncCollection.h"
#include "Image.h"
#include "GameLoop.h"
#include "KeyManager.h"
#include "FPS.h"

// Library
#pragma comment(lib, "msimg32.lib")
#pragma comment(lib, "winmm.lib")

#endif