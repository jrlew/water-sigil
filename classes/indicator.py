"""
Placeholder
"""

import os
import pygame
from .unit import Unit

WHITE = 255, 255, 255


class Indicator(Unit):
    def __init__(self, init_pos):
        Unit.__init__(self, init_pos)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/images/indicator.png")).convert()
        self.image.set_colorkey(WHITE)
