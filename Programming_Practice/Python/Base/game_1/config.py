import pygame
import enum

# Color
WHITE       = (255, 255, 255)
GRAY        = ( 50,  50,  50)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
ORANGE      = (255, 153,   0)
YELLOW      = (255, 255,   0)
GREEN       = ( 51, 255,  51)
BLUE        = (  0,   0, 255)
LIGHTBLUE   = ( 51, 255, 255)
PUPPLE      = (153,   0, 204)
SHADOW      = (130, 130, 130)

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (800, 600)
pygame.display.set_caption("Game Title")

TARGET_FPS = 60

class GameState(enum.Enum):
    GAME_PLAY = 1,
    GAME_OVER = 2

class Four_direction(enum.Enum):
    DOWN = 0
    LEFT = 1
    UP = 2
    RIGHT = 3

class Eight_direction(enum.Enum):
    DOWN = 0
    LEFTDOWN = 1
    LEFT = 2
    LEFTUP = 3
    UP = 4
    RIGHTUP = 5
    RIGHT = 6
    RIGHTDOWN = 7