#ifndef __IMAGE_H__
#define __IMAGE_H__
#include "stdafx.h"

// Allocate
GameImage* NewImage();
void Dtor_Image(GameImage* this);

// Func Pointer
HRESULT ImageInit_Set(GameImage* this, int _width, int _height);
HRESULT ImageInit_Scale(GameImage* this, LPCTSTR _fileName, int _width, int _height);
HRESULT ImageInit_Scale_Pos(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height);
HRESULT ImageInit_Scale_Pos_Trans(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height, bool _isTrans, COLORREF _transColor);
HRESULT ImageInit_Frame(GameImage* this, LPCTSTR _fileName, int _width, int _height, int _frameX, int _frameY, bool _isTrans, COLORREF _transColor);
HRESULT ImageInit_Frame_Pos(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height, int _frameX, int _frameY, bool _isTrans, COLORREF _transColor);

void ReleaseImage(GameImage* this);

void ImageRender(GameImage* this, HDC hdc);
void ImageRender_Pos(GameImage* this, HDC hdc, int destX, int destY);
void ImageRender_Pos_Scale(GameImage* this, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight);
void ImageAlphaRender(GameImage* this, HDC hdc, BYTE alpha);
void ImageAlphaRender_Pos(GameImage* this, HDC hdc, int destX, int destY, BYTE alpha);
void ImageAlphaRender_Pos_Scale(GameImage* this, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight, BYTE alpha);
void ImageFrameRender_Pos(GameImage* this, HDC hdc, int destX, int destY);
void ImageFrameRender_Pos_Set(GameImage* this, HDC hdc, int destX, int destY, int curFrameX, int curFrameY);
void ImageAlphaFrameRender_Pos_Set(GameImage* this, HDC hdc, int destX, int destY, int curFrameX, int curFrameY, BYTE alpha);

#endif