import pygame as pg

from ..store import Store
from ..units.player import Player
from .state import State


# TODO: Find a better name for this
# Phase for Non-Paired Indicator
class PlayerPhase(State):
    def __init__(self):
        super(PlayerPhase, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()
        self.font = pg.font.Font(None, 24)

    def startup(self):
        print('Player Phase Beginning')

        for unit in self.store.players:
            if unit.stats.remaining_movement:
                unit.active = True
            else:
                unit.active = False
        for unit in self.store.enemys:
            unit.active = False

        playerTurn = False
        for player in self.store.players:
            if player.stats.remaining_movement > 0:
                playerTurn = True

        if not playerTurn:
            print("Player Turn should end now")
            self.done = True
            self.next_state = "EnemyPhase"

    def get_event(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.store.indicator.up()
            elif event.key == pg.K_DOWN:
                self.store.indicator.down()
            elif event.key == pg.K_RIGHT:
                self.store.indicator.right()
            elif event.key == pg.K_LEFT:
                self.store.indicator.left()
            elif event.key == pg.K_RETURN:
                if isinstance(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x], Player):
                    self.store.paired_unit = self.store.units[self.store.indicator.position.y][self.store.indicator.position.x]
                    print(self.store.paired_unit.stats.name)
                    self.done = True
                    self.next_state = "UnitPhase"

    def update(self, dt):
        pass

    def draw(self):
        # TODO: Clean up duplication between player phases
        # Resetting old square and setting up new square
        self.store.screen.render_square(self.store.indicator.prev_position.x, self.store.indicator.prev_position.y)
        self.store.screen.render_square(self.store.indicator.position.x, self.store.indicator.position.y)

        # Clear old info and setup new
        self.store.screen.clear_info_pane()
        self.store.screen.display_terrain_info(self.store.terrain[self.store.indicator.position.y][self.store.indicator.position.x])
        if not self.store.units[self.store.indicator.position.y][self.store.indicator.position.x] == 0:
            self.store.screen.display_unit_info(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x].stats)
