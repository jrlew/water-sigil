import pygame
import os
from .unit import Unit

class Player(Unit):
    def __init__(self, initPos):
        Unit.__init__(self, initPos)
        self.image = pygame.image.load(os.path.join(
            os.path.dirname(__file__), "../data/blue.png"))
        self.rect = self.image.get_rect()
        self.maxhp = 20
        self.hp = 18
        self.strength = 6
        self.defense = 3

    def getStats(self):
        return {
            "maxhp": self.maxhp,
            "hp": self.hp,
            "strength": self.strength,
            "defense": self.defense
        }
