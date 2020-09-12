#include "GameLoop.h"

GameLoop* NewGameLoop()
{
	GameLoop* pGame = (GameLoop*)malloc(sizeof(GameLoop));

	pGame->Init = GameInit;
	pGame->Release = GameRelease;
	pGame->Update = GameUpdate;
	pGame->Render = GameRender;

	Ctor_GameLoop();

	return pGame;
}

void Ctor_GameLoop()
{
}

void Dtor_GameLoop()
{
}

HRESULT GameInit()
{	
	isDebug = false;

	timeMng = NewTimeManager();

	gameState = Proceed;
	sceneKind = Title;
	// Instance Constructor Call
	titleScene = NewTitleScene();
	stage1_Scene = NewStage1Scene();
	stage2_Scene = NewStage2Scene();

	currentScene = titleScene;

	timeMng->Init(timeMng); // FPS Initialize
	
	// *********************** Make BackBuffer for Double Buffering
	if (backBuffer == NULL)
	{
		backBuffer = NewImage();
		backBuffer->Init_Set(backBuffer,
			WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT);
	}
	// *********************** Make BackBuffer for Double Buffering

	// Image Info Initialize
	currentScene->Init();

	return S_OK;
}

void GameRelease()
{
	currentScene->Release();
}

void GameUpdate()
{
	InvalidateRect(g_hWnd, NULL, FALSE);

	if (GetKeyDown('D'))
		isDebug = !isDebug;

	currentScene->Update();
}

void GameRender()
{	
	// ����� DC�� �������
	PatBlt(backBuffer->imageInfo->hMemDC, 0, 0, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, WHITENESS);

	currentScene->Render();

	/* ������Ʈ ���ҽ� ���� �̽� �ľ� �ʿ�
	//SelectObject(imageInfo->hMemDC, imageInfo->hOldBitmap);
	//DeleteObject(imageInfo->hOldBitmap);
	*/

	if (isDebug)
		timeMng->Render(timeMng, backBuffer->imageInfo->hMemDC);

	// ���� DC�� ����
	BitBlt(hdc, 0, 0, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, backBuffer->imageInfo->hMemDC, 0, 0, SRCCOPY);

	//SelectObject(backBuffer->hMemDC, backBuffer->hOldBitmap); // ������Ʈ ���ҽ� ���� �̽� �ľ� �ʿ�
	//ReleaseDC(g_hWnd, hdc);
	//DeleteDC(backBuffer->hMemDC); // ������Ʈ ���ҽ� ���� �̽� �ľ� �ʿ�
}

//  ����:  �� â�� �޽����� ó���մϴ�.
//
//  WM_PAINT    - �� â�� �׸��ϴ�.
//  WM_DESTROY  - ���� �޽����� �Խ��ϰ� ��ȯ�մϴ�.
LRESULT MainGameProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	PAINTSTRUCT ps;

	switch (message)
	{
	case WM_CREATE:
		break;
	case WM_KEYDOWN:
	{
		switch (wParam)
		{
		case VK_ESCAPE:
			PostQuitMessage(0);
			break;
		}
	}
	break;
	case WM_MOUSEMOVE:
		g_ptMouse.x = LOWORD(lParam);
		g_ptMouse.y = HIWORD(lParam);
		break;
	break;
	case WM_TIMER:
		GameUpdate();
		break;
	case WM_PAINT:
	{
		hdc = BeginPaint(hWnd, &ps);
		//// TODO: ���⿡ hdc�� ����ϴ� �׸��� �ڵ带 �߰��մϴ�.
		GameRender();
		EndPaint(hWnd, &ps);
	}
	break;
	case WM_DESTROY:
	case WM_QUIT:
	case WM_CLOSE:
		GameRelease();
		PostQuitMessage(0);
		break;
	}
	return DefWindowProc(hWnd, message, wParam, lParam);
}