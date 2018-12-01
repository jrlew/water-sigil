import pygame as pg

class UnitPhase(object):
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
        print("Entering UnitPhase")
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist.indicator.up()
                self.persist.paired_unit.up(self.persist.units)
            elif event.key == pg.K_DOWN:
                self.persist.indicator.down()
                self.persist.paired_unit.down(self.persist.units)
            elif event.key == pg.K_RIGHT:
                self.persist.indicator.right()
                self.persist.paired_unit.right(self.persist.units)
            elif event.key == pg.K_LEFT:
                self.persist.indicator.left()
                self.persist.paired_unit.left(self.persist.units)

    def update(self, dt):
        if self.persist.paired_unit.stats.remaining_movement == 0:
            print("Change state")
            self.done = True
            self.next_state = "UnitAttackPhase"

    def draw(self, screen):
        # TODO: Duplication with PlayerPhase
        # Clean Up Previoius Square 
        screen.render_terrain(self.persist.terrain[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x], self.persist.indicator.prev_position.x, self.persist.indicator.prev_position.y)
        # if not self.persist.units[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x] == 0:
            # screen.render_unit(self.persist.units[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x])        
        screen.clear_info_pane()

        # Do The New Square
        screen.render_terrain(self.persist.terrain[self.persist.indicator.position.y][self.persist.indicator.position.x], self.persist.indicator.position.x, self.persist.indicator.position.y)        
        screen.display_terrain_info(self.persist.terrain[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x])
        # if not self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x] == 0:
        screen.display_unit_info(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x].stats)
        # screen.display_unit_info(self.persist.paired_unit)
        screen.render_unit(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x])
        # screen.render_unit(self.persist.paired_unit)
        screen.render_unit(self.persist.indicator)
