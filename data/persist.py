import pygame as pg
from .screen import Screen
from .indicator import Indicator
from .player import Player


class Persist():
    def __init__(self):
        self.screen: Screen

        self.terrain: list
        self.units: list
        self.highlights: list

        self.PIXEL_SIZE: int

        self.indicator: Indicator

        self.players: pg.sprite.Group
        self.enemys: pg.sprite.Group
        self.all_units: pg.sprite.Group

        self.paired_unit: Player

