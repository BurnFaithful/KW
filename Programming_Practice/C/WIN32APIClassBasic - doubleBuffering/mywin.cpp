#include "stdafx.h"

C_MYWIN* C_MYWIN::m_pMyWin = nullptr;

C_MYWIN::C_MYWIN() : 
	m_hInstance(NULL),
	m_hWnd(NULL),
	m_arKeyEvent{},
	m_fPosX(0.0f),
	m_fPosY(0.0f),
	m_hBmpBuffer(NULL),
	m_hBmpBackGround(NULL),
	m_hBmpChar(NULL),
	m_hBmpEnemy(NULL),
	m_btSize{}
{
}

void C_MYWIN::createWin()
{
	if (!m_pMyWin)
		m_pMyWin = new C_MYWIN();
}

C_MYWIN * C_MYWIN::getWin()
{
	return m_pMyWin	;
}

void C_MYWIN::releaseWin()
{
	if (m_pMyWin) {
		delete m_pMyWin;
		m_pMyWin = nullptr;
	}
}

bool C_MYWIN::init(HINSTANCE hInstance)
{
	//윈도우 클래스 등록
	WNDCLASSEXW wcex;
	wcex.cbSize = sizeof(WNDCLASSEX);
	wcex.style = CS_HREDRAW | CS_VREDRAW;
	wcex.lpfnWndProc = wndProc;
	wcex.cbClsExtra = 0;
	wcex.cbWndExtra = 0;
	wcex.hInstance = hInstance;
	wcex.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_WIN32APICLASSBASICDOUBLEBUFFERING));
	wcex.hCursor = LoadCursor(nullptr, IDC_ARROW);
	wcex.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
	wcex.lpszMenuName = 0;
	wcex.lpszClassName = L"className";
	wcex.hIconSm = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));
	RegisterClassExW(&wcex);


	//윈도우 생성
	m_hWnd = CreateWindowW(L"className", nullptr, WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, nullptr, nullptr, hInstance, nullptr);

	if (!m_hWnd)
		return false;

	//초기화 작업은 여기에
	m_hInstance = hInstance;

	m_hBmpBuffer	 = (HBITMAP)LoadImage(m_hInstance, L"bmp/bufferimage.bmp", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
	m_hBmpBackGround = (HBITMAP)LoadImage(m_hInstance, L"bmp/background.bmp", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
	m_hBmpChar		 = (HBITMAP)LoadImage(m_hInstance, L"bmp/char.bmp", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);
	m_hBmpEnemy		 = (HBITMAP)LoadImage(m_hInstance, L"bmp/enemy.bmp", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE);


	ShowWindow(m_hWnd, SW_SHOWDEFAULT);
	UpdateWindow(m_hWnd);

	return true;
}

void C_MYWIN::updateMsg()
{
	MSG msg = {};
	while (true)
	{
		while (PeekMessage(&msg, 0, 0, 0, PM_REMOVE))
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
		if (msg.message == WM_QUIT)
		{
			break;
		}

		//업데이트
		if (m_arKeyEvent[VK_LEFT]) {
			m_fPosX -= 0.1f;
		}
		if (m_arKeyEvent[VK_RIGHT]) {
			m_fPosX += 0.1f;
		}
		if (m_arKeyEvent[VK_UP]) {
			m_fPosY -= 0.1f;
		}
		if (m_arKeyEvent[VK_DOWN]) {
			m_fPosY += 0.1f;
		}

		HDC hDcMain = GetDC(m_hWnd);


		//랜더 로직
		HDC hdcBuffer = CreateCompatibleDC(hDcMain);
		//HDC hdcBackGround = CreateCompatibleDC(hDcMain);
		//HDC hdcChar = CreateCompatibleDC(hDcMain);
		//HDC hdcEnemy = CreateCompatibleDC(hDcMain);

		SelectObject(hdcBuffer, m_hBmpBuffer);
		//SelectObject(hdcBackGround, m_hBmpBackGround);
		//SelectObject(hdcChar, m_hBmpChar);
		//SelectObject(hdcEnemy, m_hBmpEnemy);

		GetObject(m_hBmpBackGround, sizeof(BITMAP), &m_btSize);
		BitBlt(hdcBuffer, 0, 0, m_btSize.bmWidth, m_btSize.bmHeight, hdcBackGround, 0, 0, SRCCOPY);
		
		GetObject(m_hBmpChar, sizeof(BITMAP), &m_btSize);
		BitBlt(hdcBuffer, (int)m_fPosX, (int)m_fPosY, m_btSize.bmWidth, m_btSize.bmHeight, hdcChar, 0, 0, SRCCOPY);

		GetObject(m_hBmpEnemy, sizeof(BITMAP), &m_btSize);
		BitBlt(hdcBuffer, (int)m_fPosX+100, (int)m_fPosY+100, m_btSize.bmWidth, m_btSize.bmHeight, hdcEnemy, 0, 0, SRCCOPY);

		GetObject(m_hBmpBackGround, sizeof(BITMAP), &m_btSize);
		BitBlt(hDcMain, 0, 0, m_btSize.bmWidth, m_btSize.bmHeight, hdcBuffer, 0, 0, SRCCOPY);
		
		//DeleteDC(hdcChar);
		//DeleteDC(hdcBackGround);
		//DeleteDC(hdcEnemy);
		DeleteDC(hdcBuffer);


		ReleaseDC(m_hWnd, hDcMain);
	}
}

LRESULT C_MYWIN::wndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	return m_pMyWin->myProc(hWnd, message, wParam, lParam);
}

LRESULT C_MYWIN::myProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	//윈도우 메시지 처리 콜백 함수
	switch (message)
	{
	case WM_KEYDOWN:
		m_arKeyEvent[wParam] = true;
		break;
	case WM_KEYUP:
		m_arKeyEvent[wParam] = false;
		break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd, message, wParam, lParam);
	}
	return 0;
}