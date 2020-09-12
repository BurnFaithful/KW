import pygame
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface


class Player(Sprite):
    FRAME = 10

    def __init__(self):
        Sprite.__init__(self)

        self.image_name = 'image/fourdirection_sheet.png'
        self.row = 5
        self.column = 4
        self.current_frame_x = 0
        self.current_frame_y = 0
        self.sprite_sheet = pygame.image.load(self.image_name).convert()
        self.width = self.sprite_sheet.get_rect().width // self.row
        self.height = self.sprite_sheet.get_rect().height // self.column
        self.frame_time = 0
        self.move_speed = 5
        self.image = Surface((self.width, self.height))

        rect = (self.width * self.current_frame_x, self.height * self.current_frame_y, self.width, self.height)
        self.image.blit(self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.frame_time += 1
        if self.frame_time > self.FRAME:
            self.frame_time = 0
            if self.current_frame_x == self.row - 1:
                self.current_frame_x = 0
            else:
                self.current_frame_x += 1

        rect = (self.width * self.current_frame_x, self.height * self.current_frame_y, self.width, self.height)
        self.image.blit(self.sprite_sheet, (0, 0), rect)