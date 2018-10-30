import pygame
import os
from .unit import Unit

class Enemy(Unit):
    def __init__(self, initPos):
        Unit.__init__(self, initPos)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/red.png"))
        self.rect = self.image.get_rect()
        self.maxhp = 12
        self.hp = 10
        self.strength = 3
        self.defense = 2

    def getStats(self):
        return {
            "maxhp": self.maxhp,
            "hp": self.hp,
            "strength": self.strength,
            "defense": self.defense
        }