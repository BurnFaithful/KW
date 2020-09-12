#include "Image.h"

GameImage* NewImage()
{
	GameImage* pGameImage = (GameImage*)malloc(sizeof(GameImage));

	pGameImage->Init_Set = ImageInit_Set;
	pGameImage->Init_Scale = ImageInit_Scale;
	pGameImage->Init_Scale_Pos = ImageInit_Scale_Pos;
	pGameImage->Init_Scale_Pos_Trans = ImageInit_Scale_Pos_Trans;

	pGameImage->Init_Frame = ImageInit_Frame;
	pGameImage->Init_Frame_Pos = ImageInit_Frame_Pos;

	pGameImage->Release = ReleaseImage;

	pGameImage->Render = ImageRender;
	pGameImage->Render_Pos = ImageRender_Pos;
	pGameImage->Render_Pos_Scale = ImageRender_Pos_Scale;

	pGameImage->AlphaRender = ImageAlphaRender;
	pGameImage->AlphaRender_Pos = ImageAlphaRender_Pos;
	pGameImage->AlphaRender_Pos_Scale = ImageAlphaRender_Pos_Scale;

	pGameImage->FrameRender_Pos = ImageFrameRender_Pos;
	pGameImage->FrameRender_Pos_Set = ImageFrameRender_Pos_Set;

	pGameImage->AlphaFrameRender_Pos_Set = ImageAlphaFrameRender_Pos_Set;

	return pGameImage;
}

void Dtor_Image(GameImage* this)
{
}

HRESULT ImageInit_Set(GameImage* this, int _width, int _height)
{
	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->id = 0;
	this->imageInfo->x = 0;
	this->imageInfo->y = 0;
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc);
	this->imageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc, _width, _height);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject
	(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;

	if (this->imageInfo->image == 0)
	{
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->id = 0;
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc, _width, _height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject
	(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}

HRESULT ImageInit_Scale(GameImage* this, LPCTSTR _fileName, int _width, int _height)
{
	//if (this->imageInfo != NULL) this->Release(this);

	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	// 비트맵 속성으로 파일을 불러오고 HBITMAP으로 형변환해서 hImage에 저장한다
	// fuLoad 속성 : 리소스 대신 파일명, 호환 비트맵이 아닌 DIB 섹션 비트맵으로 불러옴
	this->imageInfo->image = (HBITMAP)LoadImage(g_hInst, _fileName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->id = 0;
	this->imageInfo->x = 0;
	this->imageInfo->y = 0;
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;
	
	int len = _tcslen(_fileName);
	this->fileName = malloc(sizeof(WCHAR) * (len + 1));
	_tcscpy(this->fileName, _fileName);

	this->isTrans = false;
	this->transColor = RGB(0, 0, 0);

	if (this->imageInfo->image == 0) // 이미지를 불러오지 못했을 경우
	{
		MessageBox(g_hWnd, _T("이미지 로드 실패"), _T("이미지 로드 실패"), MB_OK);
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc/*backBuffer->imageInfo->hMemDC*/, this->imageInfo->width, this->imageInfo->height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}

HRESULT ImageInit_Scale_Pos(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height)
{
	//if (this->imageInfo != NULL) this->Release(this);

	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	// 비트맵 속성으로 파일을 불러오고 HBITMAP으로 형변환해서 hImage에 저장한다
	// fuLoad 속성 : 리소스 대신 파일명, 호환 비트맵이 아닌 DIB 섹션 비트맵으로 불러옴
	this->imageInfo->image = (HBITMAP)LoadImage(g_hInst, _fileName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->id = 0;
	this->imageInfo->x = _x;
	this->imageInfo->y = _y;
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;

	int len = _tcslen(_fileName);
	this->fileName = malloc(sizeof(WCHAR) * (len + 1));
	_tcscpy(this->fileName, _fileName);

	this->isTrans = false;
	this->transColor = RGB(0, 0, 0);

	if (this->imageInfo->image == 0) // 이미지를 불러오지 못했을 경우
	{
		MessageBox(g_hWnd, _T("이미지 로드 실패"), _T("이미지 로드 실패"), MB_OK);
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc/*backBuffer->imageInfo->hMemDC*/, this->imageInfo->width, this->imageInfo->height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}
HRESULT ImageInit_Scale_Pos_Trans(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height, bool _isTrans, COLORREF _transColor)
{
	//if (this->imageInfo != NULL) this->Release(this);

	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	// 비트맵 속성으로 파일을 불러오고 HBITMAP으로 형변환해서 hImage에 저장한다
	// fuLoad 속성 : 리소스 대신 파일명, 호환 비트맵이 아닌 DIB 섹션 비트맵으로 불러옴
	this->imageInfo->image = (HBITMAP)LoadImage(g_hInst, _fileName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->id = 0;
	this->imageInfo->x = _x;
	this->imageInfo->y = _y;
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;

	int len = _tcslen(_fileName);
	this->fileName = malloc(sizeof(WCHAR) * (len + 1));
	_tcscpy(this->fileName, _fileName);

	this->isTrans = _isTrans;
	this->transColor = _transColor;

	if (this->imageInfo->image == 0) // 이미지를 불러오지 못했을 경우
	{
		MessageBox(g_hWnd, _T("이미지 로드 실패"), _T("이미지 로드 실패"), MB_OK);
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc/*backBuffer->imageInfo->hMemDC*/, this->imageInfo->width, this->imageInfo->height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}

HRESULT ImageInit_Frame(GameImage* this, LPCTSTR _fileName, int _width, int _height, int _frameX, int _frameY, bool _isTrans, COLORREF _transColor)
{
	//if (this->imageInfo != NULL) this->Release(this);

	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	// 비트맵 속성으로 파일을 불러오고 HBITMAP으로 형변환해서 hImage에 저장한다
	// fuLoad 속성 : 리소스 대신 파일명, 호환 비트맵이 아닌 DIB 섹션 비트맵으로 불러옴
	this->imageInfo->image = (HBITMAP)LoadImage(g_hInst, _fileName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->id = 0;
	this->imageInfo->x = 0;
	this->imageInfo->y = 0;
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;

	this->imageInfo->curFrameX = 0;
	this->imageInfo->curFrameY = 0;
	this->imageInfo->maxFrameX = _frameX - 1;
	this->imageInfo->maxFrameY = _frameY - 1;
	this->imageInfo->frameWidth = _width / _frameX;
	this->imageInfo->frameHeight = _height / _frameY;

	int len = _tcslen(_fileName);
	this->fileName = malloc(sizeof(WCHAR) * (len + 1));
	_tcscpy(this->fileName, _fileName);

	this->isTrans = _isTrans;
	this->transColor = _transColor;

	if (this->imageInfo->image == 0) // 이미지를 불러오지 못했을 경우
	{
		MessageBox(g_hWnd, _T("이미지 로드 실패"), _T("이미지 로드 실패"), MB_OK);
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc/*backBuffer->imageInfo->hMemDC*/, this->imageInfo->width, this->imageInfo->height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}

HRESULT ImageInit_Frame_Pos(GameImage* this, LPCTSTR _fileName, int _x, int _y, int _width, int _height, int _frameX, int _frameY, bool _isTrans, COLORREF _transColor)
{
	//if (this->imageInfo != NULL) this->Release(this);

	HDC hdc = GetDC(g_hWnd);

	this->imageInfo = (Image*)malloc(sizeof(Image));
	this->imageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	// 비트맵 속성으로 파일을 불러오고 HBITMAP으로 형변환해서 hImage에 저장한다
	// fuLoad 속성 : 리소스 대신 파일명, 호환 비트맵이 아닌 DIB 섹션 비트맵으로 불러옴
	this->imageInfo->image = (HBITMAP)LoadImage(g_hInst, _fileName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	this->imageInfo->hOldBitmap = (HBITMAP)SelectObject(this->imageInfo->hMemDC, this->imageInfo->image);
	this->imageInfo->id = 0;
	this->imageInfo->x = _x;
	this->imageInfo->y = _y;
	this->imageInfo->width = _width;
	this->imageInfo->height = _height;

	this->imageInfo->curFrameX = 0;
	this->imageInfo->curFrameY = 0;
	this->imageInfo->maxFrameX = _frameX - 1;
	this->imageInfo->maxFrameY = _frameY - 1;
	this->imageInfo->frameWidth = _width / _frameX;
	this->imageInfo->frameHeight = _height / _frameY;

	int len = _tcslen(_fileName);
	this->fileName = malloc(sizeof(WCHAR) * (len + 1));
	_tcscpy(this->fileName, _fileName);

	this->isTrans = _isTrans;
	this->transColor = _transColor;

	if (this->imageInfo->image == 0) // 이미지를 불러오지 못했을 경우
	{
		MessageBox(g_hWnd, _T("이미지 로드 실패"), _T("이미지 로드 실패"), MB_OK);
		this->Release(this);
		return E_FAIL;
	}

	this->blendImageInfo = (Image*)malloc(sizeof(Image));
	this->blendImageInfo->hMemDC = CreateCompatibleDC(hdc/*backBuffer->imageInfo->hMemDC*/);
	this->blendImageInfo->image = (HBITMAP)CreateCompatibleBitmap(hdc/*backBuffer->imageInfo->hMemDC*/, this->imageInfo->width, this->imageInfo->height);
	this->blendImageInfo->hOldBitmap = (HBITMAP)SelectObject(this->blendImageInfo->hMemDC, this->blendImageInfo->image);
	this->blendImageInfo->width = WINDOW_SIZE_WIDTH;
	this->blendImageInfo->height = WINDOW_SIZE_HEIGHT;

	this->blendFunc.BlendFlags = 0;
	this->blendFunc.AlphaFormat = 0;
	this->blendFunc.BlendOp = AC_SRC_OVER;

	if (this->blendImageInfo == NULL)
	{
		this->Release(this);
		return E_FAIL;
	}

	ReleaseDC(g_hWnd, hdc);

	return S_OK;
}

void ReleaseImage(GameImage* this)
{
	if (this)
	{
		if (this->imageInfo)
		{
			SelectObject(this->imageInfo->hMemDC, this->imageInfo->hOldBitmap);
			DeleteObject(this->imageInfo->hOldBitmap);
			DeleteDC(this->imageInfo->hMemDC);

			free(this->imageInfo);
			this->imageInfo = NULL;

			free(this->fileName);
			this->fileName = NULL;

			this->isTrans = false;
			this->transColor = RGB(0, 0, 0);
		}
		//free(this);
		//this = NULL;
	}

	//if ((*this)->blendImageInfo)
	//{
	//	free((*this)->blendImageInfo);
	//	(*this)->blendImageInfo = NULL;
	//}
}

void ImageRender(GameImage* this, HDC hdc)
{
	if (this->isTrans)
	{
		GdiTransparentBlt(hdc, 
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->imageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, 
			this->imageInfo->height,
			this->transColor);
	}
	else
	{
		BitBlt(hdc, 
			0, 0,
			this->imageInfo->width, this->imageInfo->height, 
			this->imageInfo->hMemDC, 
			0, 0, 
			SRCCOPY);
	}
}
void ImageRender_Pos(GameImage* this, HDC hdc, int destX, int destY)
{
	if (this->isTrans)
	{
		GdiTransparentBlt(hdc,
			destX, destY,
			this->imageInfo->width, this->imageInfo->height,
			this->imageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->transColor);
	}
	else
	{
		BitBlt(hdc, 
			destX, destY,
			this->imageInfo->width, this->imageInfo->height,
			this->imageInfo->hMemDC, 
			0, 0, 
			SRCCOPY);
	}

}
void ImageRender_Pos_Scale(GameImage* this, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight)
{
	if (this->isTrans)
	{
		GdiTransparentBlt(hdc,
			destX, destY,
			sourWidth, sourHeight,
			this->imageInfo->hMemDC,
			sourX, sourY,
			this->imageInfo->width, this->imageInfo->height,
			this->transColor);
	}
	else
	{
		BitBlt(hdc, 
			destX, destY,
			sourWidth, sourHeight, 
			this->imageInfo->hMemDC, 
			sourX, sourY, 
			SRCCOPY);
	}
}
void ImageAlphaRender(GameImage* this, HDC hdc, BYTE alpha)
{
	this->blendFunc.SourceConstantAlpha = alpha;

	if (this->isTrans)
	{
		BitBlt(this->blendImageInfo->hMemDC, 
			0, 0,
			this->blendImageInfo->width, this->blendImageInfo->height,
			hdc, 
			0, 0, 
			SRCCOPY);

		GdiTransparentBlt(this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->imageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->transColor);
		AlphaBlend(hdc,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendFunc);
	}
	else
	{
		AlphaBlend(hdc,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendFunc);
	}
}
void ImageAlphaRender_Pos(GameImage* this, HDC hdc, int destX, int destY, BYTE alpha)
{
	this->blendFunc.SourceConstantAlpha = alpha;

	if (this->isTrans)
	{
		BitBlt(this->blendImageInfo->hMemDC, 
			0, 0,
			this->blendImageInfo->width,
			this->blendImageInfo->height,
			hdc, 
			destX, destY, 
			SRCCOPY);

		GdiTransparentBlt(this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->imageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->transColor);
		AlphaBlend(hdc,
			destX, destY,
			this->imageInfo->width, this->imageInfo->height,
			this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendFunc);
	}
	else
	{
		AlphaBlend(hdc,
			destX, destY,
			this->imageInfo->width, this->imageInfo->height,
			this->blendImageInfo->hMemDC,
			0, 0,
			this->imageInfo->width, this->imageInfo->height,
			this->blendFunc);
	}
}
void ImageAlphaRender_Pos_Scale(GameImage* this, HDC hdc, int destX, int destY, int sourX, int sourY, int sourWidth, int sourHeight, BYTE alpha)
{
	this->blendFunc.SourceConstantAlpha = alpha;

	if (this->isTrans)
	{
		BitBlt(this->blendImageInfo->hMemDC, 
			0, 0,
			this->blendImageInfo->width,
			this->blendImageInfo->height,
			hdc, 
			destX, destY, 
			SRCCOPY);

		GdiTransparentBlt(this->blendImageInfo->hMemDC,
			0, 0,
			sourWidth, sourHeight,
			this->imageInfo->hMemDC,
			sourX, sourX,
			sourWidth, sourHeight,
			this->transColor);
		AlphaBlend(hdc,
			destX, destY,
			sourWidth, sourHeight,
			this->blendImageInfo->hMemDC,
			0, 0,
			sourWidth, sourHeight,
			this->blendFunc);
	}
	else
	{
		AlphaBlend(hdc,
			destX, destY,
			sourWidth, sourHeight,
			this->blendImageInfo->hMemDC,
			sourX, sourY,
			sourWidth, sourHeight,
			this->blendFunc);
	}
}
void ImageFrameRender_Pos(GameImage* this, HDC hdc, int destX, int destY)
{
	if (this->isTrans)
	{
		GdiTransparentBlt(hdc,
			destX, destY,
			this->imageInfo->frameWidth, 
			this->imageInfo->frameHeight,
			this->imageInfo->hMemDC,
			this->imageInfo->curFrameX * this->imageInfo->frameWidth, 
			this->imageInfo->curFrameY * this->imageInfo->frameHeight,
			this->imageInfo->frameWidth, 
			this->imageInfo->frameHeight,
			this->transColor);
	}
	else
	{
		BitBlt(hdc, destX, destY,
			this->imageInfo->frameWidth, 
			this->imageInfo->frameHeight, 
			this->imageInfo->hMemDC, 
			this->imageInfo->curFrameX * this->imageInfo->frameWidth, 
			this->imageInfo->curFrameY * this->imageInfo->frameHeight, 
			SRCCOPY);
	}
}
void ImageFrameRender_Pos_Set(GameImage* this, HDC hdc, int destX, int destY, int curFrameX, int curFrameY)
{
	this->imageInfo->curFrameX = curFrameX;
	this->imageInfo->curFrameY = curFrameY;
	
	if (curFrameX > this->imageInfo->maxFrameX)
	{
		this->imageInfo->curFrameX = this->imageInfo->maxFrameX;
	}
	if (curFrameX > this->imageInfo->maxFrameY)
	{
		this->imageInfo->curFrameY = this->imageInfo->maxFrameY;
	}

	if (this->isTrans)
	{
		GdiTransparentBlt(hdc,
			destX, destY,
			this->imageInfo->frameWidth,
			this->imageInfo->frameHeight,
			this->imageInfo->hMemDC,
			this->imageInfo->curFrameX * this->imageInfo->frameWidth,
			this->imageInfo->curFrameY * this->imageInfo->frameHeight,
			this->imageInfo->frameWidth,
			this->imageInfo->frameHeight,
			this->transColor);
	}
	else
	{
		BitBlt(hdc, 
			destX, destY,
			this->imageInfo->frameWidth,
			this->imageInfo->frameHeight,
			this->imageInfo->hMemDC,
			this->imageInfo->curFrameX * this->imageInfo->frameWidth,
			this->imageInfo->curFrameY * this->imageInfo->frameHeight,
			SRCCOPY);
	}
}
void ImageAlphaFrameRender_Pos_Set(GameImage* this, HDC hdc, int destX, int destY, int curFrameX, int curFrameY, BYTE alpha)
{
	this->imageInfo->curFrameX = curFrameX;
	this->imageInfo->curFrameY = curFrameY;

	if (curFrameX > this->imageInfo->maxFrameX)
	{
		this->imageInfo->curFrameX = this->imageInfo->maxFrameX;
	}
	if (curFrameY > this->imageInfo->maxFrameY)
	{
		this->imageInfo->curFrameY = this->imageInfo->maxFrameY;
	}

	ImageAlphaRender_Pos_Scale(this,
		hdc,
		destX, destY,
		this->imageInfo->curFrameX * this->imageInfo->frameWidth,
		this->imageInfo->curFrameY * this->imageInfo->frameHeight,
		this->imageInfo->frameWidth,
		this->imageInfo->frameHeight,
		alpha);
}