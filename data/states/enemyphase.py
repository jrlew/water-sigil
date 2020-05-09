import sys

import pygame as pg

from ..store import Store
from .state import State


class EnemyPhase(State):
    def __init__(self):
        super(EnemyPhase, self).__init__()

    def startup(self):
        for unit in self.store.players:
            unit.active = False
        for unit in self.store.enemys:
            unit.active = True

        print("Should output stuff next")

        for unit in self.store.enemys:
            unit.move_towards_player()
            self.store.screen.render_square(
                unit.prev_position.x, unit.prev_position.y)
            self.store.screen.render_square(unit.position.x, unit.position.y)

        print("Enemy Phase Begins, if it existed yet...\n >>> Sys Exist\n\n")
        self.done = True
        self.next_state = "Player_Phase"

        # TODO: Move this to a player_phase_init/begin player_phase state
        for unit in self.store.players:
            unit.active = True
            unit.stats.remaining_movement = unit.stats.movement
        for unit in self.store.enemys:
            unit.active = False
        # sys.exit()

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass
