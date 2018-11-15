import pygame as pg
from .state import State

class PlayerPhase(State):
    def __init__(self):
        super(PlayerPhase, self).__init__()
        print("Got to the player phase but nothing happens here")
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
        # print(self.persist)

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist["indicator"].up()
            elif event.key == pg.K_DOWN:
                self.persist["indicator"].down()
            elif event.key == pg.K_RIGHT:
                self.persist["indicator"].right()
            elif event.key == pg.K_LEFT:
                self.persist["indicator"].left()
            

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        pass

    def draw(self, screen):
        """
        Draw everything to the screen.
        """
        screen.render_terrain(self.persist["terrain"][self.persist["indicator"].prev_position.y][self.persist["indicator"].prev_position.x], self.persist["indicator"].prev_position.x, self.persist["indicator"].prev_position.y)
        screen.render_terrain(self.persist["terrain"][self.persist["indicator"].position.y][self.persist["indicator"].position.x], self.persist["indicator"].position.x, self.persist["indicator"].position.y)
        screen.render_unit(self.persist["indicator"])

