import sys
import random

from tetris.config import *
from tetris.block import *
from tetris.board import *

pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

tetromino = Block()
game_board = Board()

def main():
    init_game()
    pygame.quit()
    sys.exit()


def init_game():
    pygame.init()
    run_game()


def run_game():
    is_run = True
    while is_run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    if tetromino.x > BLOCK_SIZE: tetromino.x -= BLOCK_SIZE
                elif key[pygame.K_RIGHT]:
                    if tetromino.x < PLAY_WIDTH - BLOCK_SIZE - (BLOCK_SIZE * tetromino.width): tetromino.x += BLOCK_SIZE
                elif key[pygame.K_DOWN]:
                    tetromino.y += BLOCK_SIZE
                elif key[pygame.K_z]:
                    max = len(tetromino.type)
                    tetromino.rotate += 1
                    tetromino.block_data = tetromino.type[tetromino.rotate % max]
                    tetromino.width = len(tetromino.block_data[0])
                    tetromino.height = len(tetromino.block_data)


        tetromino.update()

        SCREEN.fill(BLACK)
        game_board.draw()
        tetromino.draw()
        pygame.display.flip()

        clock.tick(TARGET_FPS)


if __name__ == "__main__":
    main()
