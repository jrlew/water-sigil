"""
Placeholder
"""

import os
import pygame
from .unit import Unit

WHITE = 255, 255, 255

class Indicator(Unit):
    def __init__(self, init_pos_tuple):
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/common/indicator.png")).convert()
        self.image.set_colorkey(WHITE)


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1] 
