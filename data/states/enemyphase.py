import sys
import pygame as pg
from .state import State

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
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

        for unit in self.persist.players:
            unit.active = False
        for unit in self.persist.enemys:
            unit.active = True

        print("Enemy Phase Begins, if it existed yet...\n >>> Sys Exist")
        sys.exit()

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

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass
