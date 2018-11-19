import pygame as pg
from ..enemy import Enemy
class UnitAttackPhase(object):
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
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        print("Got to the attack state")
        self.persist = persistent
        self.persist["paired_unit"].display_attack_overlay(self.persist["screen"])

    def get_event(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist["indicator"].up()
            elif event.key == pg.K_DOWN:
                self.persist["indicator"].down()
            elif event.key == pg.K_RIGHT:
                self.persist["indicator"].right()
            elif event.key == pg.K_LEFT:
                self.persist["indicator"].left()
            # TODO: Move to enemy turn
            elif event.key == pg.K_RETURN:
                if isinstance(self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x], Enemy):
                    self.persist["paired_unit"].attack(
                        self.persist["screen"],
                        self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x],
                        self.persist["terrain"][self.persist["indicator"].position.y][self.persist["indicator"].position.x]
                    )
                elif self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x] == self.persist["paired_unit"]:
                    print("This should end the players turn")

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        pass

    def draw(self, screen):
        # TODO: Clean up duplication between player phases
        # TODO: Fix Attack Overlay disappearing
        # Clean Up Previoius Square 
        screen.render_terrain(self.persist["terrain"][self.persist["indicator"].prev_position.y][self.persist["indicator"].prev_position.x], self.persist["indicator"].prev_position.x, self.persist["indicator"].prev_position.y)
        if not self.persist["units"][self.persist["indicator"].prev_position.y][self.persist["indicator"].prev_position.x] == 0:
            screen.render_unit(self.persist["units"][self.persist["indicator"].prev_position.y][self.persist["indicator"].prev_position.x])        
        screen.clear_info_pane()

        # Do The New Square
        screen.render_terrain(self.persist["terrain"][self.persist["indicator"].position.y][self.persist["indicator"].position.x], self.persist["indicator"].position.x, self.persist["indicator"].position.y)        
        screen.display_terrain_info(self.persist["terrain"][self.persist["indicator"].prev_position.y][self.persist["indicator"].prev_position.x])
        if not self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x] == 0:
            screen.display_unit_info(self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x].stats)
            screen.render_unit(self.persist["units"][self.persist["indicator"].position.y][self.persist["indicator"].position.x])
        screen.render_unit(self.persist["indicator"])