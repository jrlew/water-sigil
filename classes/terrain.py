"""
Placeholder
"""


import os
import pygame


class Terrain():
    def __init__(self, type, path_to_image, def_adjustment, 
evasion_adjustment):
        self.type = type
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), path_to_image)).convert()
        self.def_adjustment = def_adjustment
        self.evasion_adjustment = evasion_adjustment 
