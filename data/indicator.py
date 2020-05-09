import os

import pygame

from . import colors
from .tools.image import load_png
from .units.unit import Unit


class Indicator(Unit):
    def __init__(self, init_pos_tuple):
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.image = load_png("common/indicator.png", override_alpha=True)
        self.image.set_colorkey(colors.WHITE)

    def up(self):
        self.update_prev_position()
        self.position.y -= 1

    def down(self):
        self.update_prev_position()
        self.position.y += 1

    def left(self):
        self.update_prev_position()
        self.position.x -= 1

    def right(self):
        self.update_prev_position()
        self.position.x += 1


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1]
