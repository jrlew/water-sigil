import pygame as pg

from ..store import Store
from ..tools.image import load_png
from .state import State


class LevelSelect(State):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()
        self.font = pg.font.Font(None, 24)
        self.indicator_state = True
        self.waiting = True

    def startup(self):
        level_image = load_png("levelthumbnails/levelone.png")
        
        self.store.screen.render_image(level_image, 10, 10)
        self.store.screen.display_context_message("> Level One     Level Two")

        pg.display.update()

    def get_event(self, event):
        if event.type == pg.QUIT:
            sys.quit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                self.indicator_state = not self.indicator_state
                if self.indicator_state:
                    self.store.screen.display_context_message(
                        ">Level One    Level Two")
                else:
                    self.store.screen.display_context_message(
                        " Level One   >Level Two")
                pg.display.update()
            if event.key == pg.K_RETURN:
                self.done = True
                self.next_state = "Level_Init"

    def update(self, dt):
        pass

    def draw(self):
        pass
