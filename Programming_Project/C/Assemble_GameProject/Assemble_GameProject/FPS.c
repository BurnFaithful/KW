#include "FPS.h"

Frame* NewTimeManager()
{
	Frame* pFrame = (Frame*)malloc(sizeof(Frame));

	pFrame->Init = FPSInit;
	pFrame->Tick = Tick;
	pFrame->Render = FPSRender;

	return pFrame;
}

HRESULT FPSInit(Frame* this)
{
	if (QueryPerformanceFrequency((LARGE_INTEGER*)&this->periodFrequency))
	{
		this->isHighPerformance = true;

		QueryPerformanceCounter((LARGE_INTEGER*)&this->lastTime);

		this->timeScale = 1.0f / this->periodFrequency;
	}
	else
	{
		this->isHighPerformance = false;

		this->lastTime = timeGetTime();
		this->timeScale = 1.0f / 1000;
	}

	this->frameRate = 0;
	this->fpsFrameCount = 0;
	this->fpsElapsedTime = 0.f;
	this->worldTime = 0.f;

	return S_OK;
}

void Tick(Frame* this, float lockFPS)
{
	if (this->isHighPerformance)
	{
		QueryPerformanceCounter((LARGE_INTEGER*)&this->curTime);
	}
	else
	{
		this->curTime = timeGetTime();
	}

	this->elapsedTime = (this->curTime - this->lastTime) * this->timeScale;

	if (lockFPS)
	{
		while (this->elapsedTime < (1.f / lockFPS))
		{
			if (this->isHighPerformance)
			{
				QueryPerformanceCounter((LARGE_INTEGER*)&this->curTime);
			}
			else
			{
				this->curTime = timeGetTime();
			}

			this->elapsedTime = (this->curTime - this->lastTime) * this->timeScale;
		}
	}

	this->lastTime = this->curTime;
	this->fpsFrameCount++;
	this->fpsElapsedTime += this->elapsedTime;
	this->worldTime += this->elapsedTime;

	if (this->fpsElapsedTime > 1.f)
	{
		this->frameRate = this->fpsFrameCount;
		this->fpsFrameCount = 0;
		this->fpsElapsedTime = 0.f;
	}
}

void FPSRender(Frame* this, HDC hdc)
{
#ifdef _DEBUG
	WCHAR textStr[256];

	SetBkMode(hdc, TRANSPARENT);
	SetTextColor(hdc, RGB(0, 0, 0));

	swprintf_s(textStr, 256, _T("FPS : %d"), this->frameRate);
	TextOut(hdc, 0, 0, textStr, _tcslen(textStr));

	swprintf_s(textStr, 256, _T("worldTime : %.5f"), this->worldTime);
	TextOut(hdc, 0, 20, textStr, _tcslen(textStr));

	swprintf_s(textStr, 256, _T("elapsedTime : %.5f"), this->elapsedTime);
	TextOut(hdc, 0, 40, textStr, _tcslen(textStr));

	TextOut(hdc, 200, 0, _T("방향키 : 플레이어 이동"), _tcslen(_T("방향키 : 플레이어 이동")));
	TextOut(hdc, 500, 0, _T("D키 : 디버그모드 출력 토글"), _tcslen(_T("D키 : 디버그모드 출력 토글")));
	TextOut(hdc, 200, 20, _T("S키 : 게임 시작/다음 스테이지 시작"), _tcslen(_T("S키 : 게임 시작/다음 스테이지 시작")));
	TextOut(hdc, 500, 20, _T("R키 : 게임 재시작"), _tcslen(_T("R키 : 게임 재시작")));
#else
#endif
}