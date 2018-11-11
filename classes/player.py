"""
Placeholder
"""

import os
import pygame
from .unit import Unit


class Player(Unit):
    def __init__(self, init_pos, playerStats):
        Unit.__init__(self, init_pos, playerStats)
        self.image_active = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/images/sprites/blue-soldier.png"))
        self.image_inactive = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/images/sprites/blue-soldier-inactive.png"))
        self.image = self.image_active
        self.rect = self.image.get_rect()
