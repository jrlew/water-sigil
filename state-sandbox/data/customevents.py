import pygame as pg

class CustomEvents():
    def __init__(self):
        self.UPDATE_ANIMATION = pg.USEREVENT + 1
        self.ADVANCE_ENEMY_TURN = pg.USEREVENT + 2