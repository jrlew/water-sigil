import pygame as pg

from ..store import Store
from .state import State


class EndLevel(State):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()
        self.font = pg.font.Font(None, 24)

    def startup(self):
        print("Success! Level Complete!")
        self.done = True
        self.next_state = "Level_Select"

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass
