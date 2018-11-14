"""
Placeholder
"""

import os
import pygame
from .units.unit import Unit


class Player(Unit):
    def __init__(self, init_pos, job):
        Unit.__init__(self, init_pos, job.info)
