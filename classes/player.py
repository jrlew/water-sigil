"""
Placeholder
"""

import os
import pygame
from .unit import Unit


class Player(Unit):
    def __init__(self, init_pos, _is_player):
        Unit.__init__(self, init_pos, _is_player)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/blue.png"))
        self.rect = self.image.get_rect()
