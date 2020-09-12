from config import *
from board import Board
import random

# [block][rotation][color]
BLOCK_TEMPLATE = (
    # I
    (
        ((1, 1, 1, 1), ),
        ((1, ),
         (1, ),
         (1, ),
         (1, ))
    ),

    # O
    (
        ((2, 2),
         (2, 2)),
    ),

    # Z
    (
        ((3, 3, 0),
         (0, 3, 3)),
        ((0, 3),
         (3, 3),
         (3, 0)),
    ),

    # S
    (
        ((0, 4, 4),
         (4, 4, 0)),
        ((4, 0),
         (4, 4),
         (0, 4)),
    ),

    # J
    (
        ((0, 5),
         (0, 5),
         (5, 5)),
        ((5, 0, 0),
         (5, 5, 5)),
        ((5, 5),
         (5, 0),
         (5, 0)),
        ((5, 5, 5),
         (0, 0, 5)),
    ),

    # L
    (
        ((6, 0),
         (6, 0),
         (6, 6)),
        ((6, 6, 6),
         (6, 0, 0)),
        ((6, 6),
         (0, 6),
         (0, 6)),
        ((0, 0, 6),
         (6, 6, 6))
    ),

    # T
    (
        ((0, 7, 0),
         (7, 7, 7)),
        ((7, 0),
         (7, 7),
         (7, 0)),
        ((7, 7, 7),
         (0, 7, 0)),
        ((0, 7),
         (7, 7),
         (0, 7))
    )
)

BLOCK_SIZE = 30
ROW = 40
COL = 20

class Block:
    def __init__(self):
        self.speed = 30
        self.frame = 0

        self.type = BLOCK_TEMPLATE[random.randint(0, 6)]
        self.rotate = 0
        self.block_data = self.type[self.rotate]
        self.next_block = []

        self.width = len(self.block_data[0])
        self.height = len(self.block_data)
        self.x = PLAY_WIDTH // 2
        self.y = 0

    def update(self):
        self.frame += 1
        if self.y + (BLOCK_SIZE * self.height) < PLAY_HEIGHT - BLOCK_SIZE:
            if self.frame > self.speed:
                self.y += BLOCK_SIZE
                self.frame = 0
        else:
            self.get_new_tetromino()

    def draw(self):
        for i_index, i in enumerate(self.block_data):
            for j_index, j in enumerate(i):
                pygame.draw.rect(SCREEN, COLORS[j], pygame.Rect(
                    self.x + (BLOCK_SIZE * j_index),
                    self.y + (BLOCK_SIZE * i_index),
                    BLOCK_SIZE, BLOCK_SIZE), 0)


    def get_new_tetromino(self):
        self.type = BLOCK_TEMPLATE[random.randint(0, 6)]
        self.rotate = 0
        self.block_data = self.type[self.rotate]
        self.width = len(self.block_data[0])
        self.height = len(self.block_data)
        self.x = PLAY_WIDTH // 2
        self.y = 0

