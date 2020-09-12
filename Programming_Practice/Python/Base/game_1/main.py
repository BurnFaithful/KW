# import pygame
import sys
from config import *
from player import *

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

game_state = GameState.GAME_PLAY
player = Player()


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
                if key[pygame.K_ESCAPE]: is_run = False

        if game_state == GameState.GAME_PLAY:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if player.rect.x > 0: player.rect.x -= player.move_speed
                player.current_frame_y = Four_direction.LEFT.value
            elif keys[pygame.K_RIGHT]:
                if player.rect.x < WINDOW_WIDTH - player.width: player.rect.x += player.move_speed
                player.current_frame_y = Four_direction.RIGHT.value
            elif keys[pygame.K_UP]:
                if player.rect.y > 0: player.rect.y -= player.move_speed
                player.current_frame_y = Four_direction.UP.value
            elif keys[pygame.K_DOWN]:
                if player.rect.y < WINDOW_HEIGHT - player.height: player.rect.y += player.move_speed
                player.current_frame_y = Four_direction.DOWN.value

            screen.fill(BLACK)
            player.update()
            screen.blit(player.image, player.rect)
            pygame.display.flip()

        clock.tick(TARGET_FPS)


if __name__ == "__main__":
    main()
