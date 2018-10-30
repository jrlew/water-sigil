import pygame
import os
from .unit import Unit

white = 255, 255, 255

class Indicator(Unit):
    def __init__(self, initPos):
        Unit.__init__(self, initPos)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "../data/indicator.png")).convert()
        self.image.set_colorkey(white)
