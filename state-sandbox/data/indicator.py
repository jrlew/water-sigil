"""
Placeholder
"""

import os
import pygame
from .units.unit import Unit

WHITE = 255, 255, 255

# TODO: Separate from Unit
class Indicator(Unit):
    def __init__(self, init_pos_tuple):
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/common/indicator.png")).convert()
        self.image.set_colorkey(WHITE)

    def up(self):
        self.update_prev_position()
        self.position.y -= 1


    def down(self):
        self.update_prev_position()
        self.position.y += 1


    def left(self):
        self.update_prev_position()
        self.position.x -= 1


    def right(self):
        self.update_prev_position()
        self.position.x += 1


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1] 
