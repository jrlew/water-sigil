"""
Placeholder
"""

import os
import pygame
from .units.unit import Unit


class Player(Unit):
    def __init__(self, init_pos, job):
        Unit.__init__(self, init_pos, job.stats)
        self.image_active = job.image_active
        self.image_inactive = job.image_inactive
        self.idle_1 = job.idle_1
        self.idle_2 = job.idle_2
        self.is_idle_1 = True
        self.image = self.image_active
        self.rect = self.image.get_rect()
