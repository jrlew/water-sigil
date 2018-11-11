"""
Placeholder
"""

import os
import pygame
from .unit import Unit


class Enemy(Unit):
    def __init__(self, init_pos, job):
        Unit.__init__(self, init_pos, job.stats)
        self.image_active = job.image_active
        self.image_inactive = job.image_inactive
        self.image = self.image_active
        self.rect = self.image.get_rect()
