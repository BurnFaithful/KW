#include "Sound.h"

Sound* NewSoundManager()
{
	Sound* pSound = (Sound*)malloc(sizeof(Sound));

	pSound->LoadWav = LoadWav_Sound;
	pSound->PlayWav = PlayWav_Sound;

	return pSound;
}

DWORD LoadWav_Sound(HWND hWnd, LPCTSTR lpszWave)
{
	wDeviceID = 0;

	DWORD result;

	mciOpen.lpstrDeviceType = _T("WaveAudio");
	mciOpen.lpstrElementName = lpszWave;

	result = mciSendCommand(wDeviceID, MCI_OPEN,
		MCI_OPEN_TYPE | MCI_OPEN_ELEMENT,
		(DWORD)(LPVOID)&mciOpen);

	if (result) return result;

	wDeviceID = mciOpen.wDeviceID;

	mciPlay.dwCallback = (DWORD)hWnd;

	if (result) return result;

	return 0;
}

DWORD PlayWav_Sound(HWND hWnd, LPCTSTR lpszWave)
{
	DWORD sound;

	sound = LoadWav_Sound(hWnd, lpszWave);

	sound = mciSendCommand(mciOpen.wDeviceID, MCI_SEEK,
		MCI_SEEK_TO_START, (DWORD)(LPVOID)NULL);

	sound = mciSendCommand(mciOpen.wDeviceID, MCI_PLAY,
		MCI_NOTIFY | MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)&mciPlay);

	if (sound)
	{
		mciSendCommand(mciOpen.wDeviceID, MCI_CLOSE, 0, (DWORD)NULL);
		return sound;
	}
	else
		return 0;
}

