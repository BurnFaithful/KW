#ifndef __SOUND_H__
#define __SOUND_H__
#include "stdafx.h"

MCI_OPEN_PARMS m_mciOpenParms;
MCI_PLAY_PARMS m_mciPlayParms;
DWORD m_dwDeviceID;
MCI_OPEN_PARMS mciOpen; // File Load
MCI_PLAY_PARMS mciPlay; // File Play
MCI_STATUS_PARMS mciStatus; // File Status

UINT wDeviceID;

Sound* NewSoundManager();

DWORD LoadWav_Sound(HWND hWnd, LPCTSTR lpszWave);
DWORD PlayWav_Sound(HWND hWnd, LPCTSTR lpszWave);

#endif