import pygame as pg
from ..enemy import Enemy
from ..units import units
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
        print('Unit Attack Phase Beginning')
        self.persist = persistent
        self.persist.paired_unit.display_attack_overlay(self.persist)
        # Loop through highlighted squares to init the attack overlay
        # TODO: Look into setting up array of highlighted squares instead of looping through 2d array
        self.persist.paired_unit.cleanup_movement_highlights(self.persist)

    def get_event(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist.indicator.up()
            elif event.key == pg.K_DOWN:
                self.persist.indicator.down()
            elif event.key == pg.K_RIGHT:
                self.persist.indicator.right()
            elif event.key == pg.K_LEFT:
                self.persist.indicator.left()
            # TODO: Move to enemy turn
            elif event.key == pg.K_ESCAPE:
                self.done = True
                self.next_state = "UnitPhase"
                self.persist.paired_unit.cleanup_attack_highlights()

            elif event.key == pg.K_RETURN:
                if isinstance(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x], Enemy) and self.persist.highlights[self.persist.indicator.position.y][self.persist.indicator.position.x]:
                    self.persist.paired_unit.attack(
                        self.persist,
                        self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x],
                    )
                    # TODO: turn this back 
                    self.done = True
                    self.next_state = "Player_Phase"
                    self.persist.paired_unit.stats.remaining_movement = 0 # Temp remove after movement change
                    self.persist.paired_unit.active = False
                    # TODO: Make this function
                    self.persist.paired_unit.cleanup_attack_highlights()

                elif self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x] == self.persist.paired_unit:
                    print("This should end the units turn")
                    self.done = True
                    self.next_state = "Player_Phase"
                    self.persist.paired_unit.stats.remaining_movement = 0 # Temp remove after movement change
                    self.persist.paired_unit.active = False
                    # TODO: Make this function
                    self.persist.paired_unit.cleanup_attack_highlights()

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        pass

    def draw(self, screen):
        # TODO: Clean up duplication between player phases
        # Resetting old square and setting up new square
        screen.render_square(self.persist, self.persist.indicator.prev_position.x, self.persist.indicator.prev_position.y)
        screen.render_square(self.persist, self.persist.indicator.position.x, self.persist.indicator.position.y)

        # Clear old info and setup new
        screen.clear_info_pane()
        screen.display_terrain_info(self.persist.terrain[self.persist.indicator.position.y][self.persist.indicator.position.x])
        if not self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x] == 0:
            screen.display_unit_info(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x].stats)

