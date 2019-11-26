import pygame as pg

from ..indicator import Indicator
#TODO: fix these names....
from ..levels.two import level_params
from ..store import Store
from .state import State


# TODO: This should go away
# TODO: This and Level1 should be merged into game.py that exits back to the level select
class LevelInit(State):
    def __init__(self):
        super(LevelInit, self).__init__()
        self.done = False
        self.quit = False
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()

    def get_event(self, event):
        pass

    def update(self, dt):
        self.store.terrain = level_params["terrain"]
        self.store.indicator = Indicator((0, 0))
        self.store.enemys = level_params["enemys"]
        self.store.players = level_params["players"]
        self.store.all_units = pg.sprite.Group(self.store.players.sprites() + self.store.enemys.sprites())
        # TODO: create units based on size of terrain 
        self.store.units = [
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
        self.store.highlights = [
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
        for unit in self.store.all_units.sprites():
            self.store.units[unit.position.y][unit.position.x] = unit

    def draw(self):
        self.store.screen.init_all()
        self.store.screen.display_terrain_info(self.store.terrain[self.store.indicator.prev_position.y][self.store.indicator.prev_position.x])
        
        self.store.screen.render_indicator()
        for unit in self.store.all_units.sprites():
            self.store.screen.render_unit(unit.position.x, unit.position.y)

        self.next_state = "Player_Phase"
        self.done = True
