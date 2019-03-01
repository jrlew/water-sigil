import pygame as pg
from .state import State


class LevelSelect(State):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):


        screen.display_context_message("> Level One     Level Two")
        pg.display.update()

        indicator_state = True
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP or event.key == pg.K_DOWN:
                        indicator_state = not indicator_statev
                        if indicator_state:
                            screen.display_context_message(
                                ">Level One    Level Two")
                        else:
                            screen.display_context_message(
                                " Level One   >Level Two")
                        pg.display.update()
                    if event.key == pg.K_RETURN:
                        waiting = False

        if indicator_state:
            print('Selecting Level One')
        else:
            print('Selecting Level Two')


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
