import pygame as pg
from .state import State

from ..indicator import Indicator

#TODO: fix these names....
from ..levels.two import level_params

from ..persist import Persist

# TODO: This should go away
# TODO: This and Level1 should be merged into game.py that exits back to the level select
class LevelInit(State):
    def __init__(self):
        super(LevelInit, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = "Player_Phase"
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = Persist()
        self.font = pg.font.Font(None, 24)
        self.PIXEL_SIZE = 32
        self.indicator = Indicator((0, 0))


    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        self.persist.terrain = level_params["terrain"]
        self.persist.PIXEL_SIZE = 32
        self.persist.indicator = self.indicator
        self.persist.enemys = level_params["enemys"]
        self.persist.players = level_params["players"]
        self.persist.all_units = pg.sprite.Group(self.persist.players.sprites() + self.persist.enemys.sprites())
        # TODO: create units based on size of terrain 
        self.persist.units = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # TODO: create based on size of terrain 
        # Probably could use a better name
        self.persist.highlights = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        for unit in self.persist.all_units.sprites():
            self.persist.units[unit.position.y][unit.position.x] = unit

    def draw(self, screen):
        screen.init_info_pane()
        screen.init_context_menu()
        screen.init_screen(self.persist.terrain)
        screen.render_indicator(self.persist)
        # screen.render_unit(self.persist.indicator, self.persist.indicator.position.x, self.persist.indicator.position.y) # TODO: Indicator is a unit anymore... Maybe needs its own render functiosn
        screen.display_terrain_info(self.persist.terrain[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x])
        for unit in self.persist.all_units.sprites():
            screen.render_unit(self.persist, unit.position.x, unit.position.y)
        self.done = True
