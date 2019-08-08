import sys
import pygame as pg
from .state import State
from ..store import Store

class EnemyPhase(State):
    """
    Parent class for individual game states to inherit from. 
    """

    def __init__(self):
        super(EnemyPhase, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()
        self.font = pg.font.Font(None, 24)

    def startup(self):
        for unit in self.store.players:
            unit.active = False
        for unit in self.store.enemys:
            unit.active = True


        print("Should output stuff next")

        for unit in self.store.enemys:
            unit.move_towards_player()
            self.store.screen.render_square(unit.prev_position.x, unit.prev_position.y)
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
        """
        Handle a single event passed by the Game object.
        """
        pass

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        pass

    def draw(self):
        """
        Draw everything to the screen.
        """
        # surface.update()
        # pass
