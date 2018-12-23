"""
Placeholder
"""

import pygame
from .units.unit import Unit


class Enemy(Unit):
    def __init__(self, init_pos, job):
        Unit.__init__(self, init_pos, job.info)
