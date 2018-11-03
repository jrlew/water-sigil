"""
Placeholder
"""

import os
import pygame
from .unit import Unit

WHITE = 255, 255, 255


class Indicator(Unit):
    def __init__(self, init_pos, _is_player):
        Unit.__init__(self, init_pos, _is_player)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/indicator.png")).convert()
        self.image.set_colorkey(WHITE)
        self.paired_unit = False
