import pygame

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

COLORS = (BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PUPPLE, LIGHTBLUE, GRAY)

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (800, 600)
PLAY_SIZE = PLAY_WIDTH, PLAY_HEIGHT = (540, 600)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
GAME_TITLE = "Tetris"

TARGET_FPS = 60