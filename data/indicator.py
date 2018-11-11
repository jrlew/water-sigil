"""
Placeholder
"""

import os
import pygame
from .units.unit import Unit

WHITE = 255, 255, 255

# Separate Indicator class from Unit class
class Indicator(Unit):
    def __init__(self, init_pos, indicatorStats):
        Unit.__init__(self, init_pos, indicatorStats)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/common/indicator.png")).convert()
        self.image.set_colorkey(WHITE)
