#pragma once

#include <Windows.h>

class C_MYWIN
{
private:
	enum {
		E_KEYMAX = 0xFF + 1,
	};
private:
	static C_MYWIN* m_pMyWin;

public:
	static void createWin();
	static C_MYWIN* getWin();
	static void releaseWin();

private:
	HINSTANCE	m_hInstance;
	HWND		m_hWnd;

	HBITMAP m_hBmpBuffer;
	HBITMAP m_hBmpBackGround;
	HBITMAP m_hBmpChar;
	HBITMAP m_hBmpEnemy;
	BITMAP m_btSize;

	BYTE m_arKeyEvent[E_KEYMAX];

	float m_fPosX;
	float m_fPosY;

private:
	C_MYWIN();
	static LRESULT CALLBACK wndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);
	LRESULT CALLBACK myProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);

public:
	bool init(HINSTANCE hInstance);
	void updateMsg();

};
