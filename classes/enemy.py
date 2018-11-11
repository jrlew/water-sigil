"""
Placeholder
"""

import os
import pygame
from .unit import Unit


class Enemy(Unit):
    def __init__(self, init_pos, enemyStats):
        Unit.__init__(self, init_pos, enemyStats)
        self.image_active = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/characters/red/soldier/red-soldier.png"))
        self.image_inactive = pygame.image.load(os.path.join(os.path.dirname(__file__), "../assets/characters/red/soldier/red-soldier-inactive.png"))
        self.image = self.image_active
        self.rect = self.image.get_rect()
