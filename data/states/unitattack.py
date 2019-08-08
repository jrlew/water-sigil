import pygame as pg
from ..enemy import Enemy
from ..units import units
from ..units.unit import Position
from ..store import Store

class UnitAttackPhase(object):
    """
    Parent class for individual game states to inherit from. 
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.store = Store.instance()
        self.font = pg.font.Font(None, 24)

    def startup(self):
        print('Unit Attack Phase Beginning')

        self.store.paired_unit.display_attack_overlay()
            # Loop through highlighted squares to init the attack overlay
            # TODO: Look into setting up array of highlighted squares instead of looping through 2d array
        self.store.paired_unit.cleanup_movement_highlights()

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
            # TODO: Move to enemy turn
            elif event.key == pg.K_ESCAPE:
                pre_pos = Position([self.store.paired_unit.update_pre_pos('x'),self.store.paired_unit.update_pre_pos('y')])
                self.store.paired_unit.move_to_position(pre_pos)
                self.done = True
                self.next_state = "UnitPhase"
                self.store.paired_unit.cleanup_attack_highlights()

            elif event.key == pg.K_RETURN:
                if isinstance(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x], Enemy) and self.store.highlights[self.store.indicator.position.y][self.store.indicator.position.x]:
                    self.store.paired_unit.attack(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x])
                    # TODO: turn this back 
                    self.done = True
                    self.next_state = "Player_Phase"
                    self.store.paired_unit.stats.remaining_movement = 0 # Temp remove after movement change
                    self.store.paired_unit.active = False
                    # TODO: Make this function
                    self.store.paired_unit.cleanup_attack_highlights()

                elif self.store.units[self.store.indicator.position.y][self.store.indicator.position.x] ==self.store.paired_unit:
                    print("This should end the units turn")
                    self.done = True
                    self.next_state = "Player_Phase"
                    self.store.paired_unit.stats.remaining_movement = 0 # Temp remove after movement change
                    self.store.paired_unit.active = False
                    # TODO: Make this function
                    self.store.paired_unit.cleanup_attack_highlights()

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        pass

    def draw(self):
        # TODO: Clean up duplication between player phases
        # Resetting old square and setting up new square
        self.store.screen.render_square(self.store.indicator.prev_position.x,self.store.indicator.prev_position.y)
        self.store.screen.render_square(self.store.indicator.position.x,self.store.indicator.position.y)

        # Clear old info and setup new
        self.store.screen.clear_info_pane()
        self.store.screen.display_terrain_info(self.store.terrain[self.store.indicator.position.y][self.store.indicator.position.x])
        if not self.store.units[self.store.indicator.position.y][self.store.indicator.position.x] == 0:
            self.store.screen.display_unit_info(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x].stats)

