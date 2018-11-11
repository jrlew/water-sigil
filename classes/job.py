"""
Placeholder
"""

import os
import pygame

class Job():
    def __init__(self, info):
        # self.name = info["stats"]["name"],
        self.stats = info["stats"]
        self.image_active = pygame.image.load(os.path.join(os.path.dirname(__file__), info["image_active_path"]))
        self.image_inactive = pygame.image.load(os.path.join(os.path.dirname(__file__), info["image_inactive_path"]))
        self.image = self.image_active
