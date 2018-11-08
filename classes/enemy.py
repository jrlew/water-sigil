"""
Placeholder
"""

import os
import pygame
from .unit import Unit


class Enemy(Unit):
    def __init__(self, init_pos, enemyStats):
        Unit.__init__(self, init_pos, enemyStats)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/images/red.png"))
        self.rect = self.image.get_rect()
