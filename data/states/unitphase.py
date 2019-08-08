import pygame as pg
from ..store import Store

from ..terrain.moveoverlay import MoveOverlay

class UnitPhase(object):
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
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        print("Unit Phase Beginning")
        # TODO: Name this better and maybe make it a part of persist
        self.store.current_highlights = self.store.paired_unit.setup_movement_highlight()


    # TODO: Change this to move player on 'enter' when indicator is on highlighted square
    def get_event(self, event):
        pre_pos_x = self.store.paired_unit.update_pre_pos('x')
        pre_pos_y = self.store.paired_unit.update_pre_pos('y')
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
                if isinstance(self.store.highlights[self.store.indicator.position.y][self.store.indicator.position.x], MoveOverlay) and not self.store.units[self.store.indicator.position.y][self.store.indicator.position.x]:
                    print("Change state")
                    self.done = True
                    self.next_state = "UnitAttackPhase"
                    self.store.paired_unit.move_to_position(self.store.indicator.position)
                    for mov in self.store.current_highlights:
                        self.store.highlights[mov[1]][mov[0]] = 0
                        self.store.screen.render_square(mov[0], mov[1])
                elif self.store.paired_unit.position.x == self.store.indicator.position.x and self.store.paired_unit.position.y == self.store.indicator.position.y:
                    print("Ending Turn No Movement")
                    self.done = True
                    self.next_state = "UnitAttackPhase"
                    for mov in self.store.current_highlights:
                        self.store.highlights[mov[1]][mov[0]] = 0
                        self.store.screen.render_square(mov[0], mov[1])
                else:
                    self.store.screen.display_context_message("Unable To Move Units To Selected Tile")
            elif event.key == pg.K_ESCAPE:
                print("backout completed")
                for mov in self.store.current_highlights:
                        self.store.highlights[mov[1]][mov[0]] = 0
                        self.store.screen.render_square(mov[0], mov[1])
                self.store.paired_unit.cleanup_movement_highlights()
                self.done = True
                self.next_state = "Player_Phase"
                
                


    def update(self, dt):
        pass


    def draw(self):
        # TODO: Don't draw every tick.... somehow
        # Resetting old square and setting up new square
        self.store.screen.render_square(self.store.indicator.prev_position.x, self.store.indicator.prev_position.y)
        self.store.screen.render_square(self.store.indicator.position.x, self.store.indicator.position.y)

        # Clear old info and setup new
        self.store.screen.clear_info_pane()
        self.store.screen.display_terrain_info(self.store.terrain[self.store.indicator.position.y][self.store.indicator.position.x])
        if not self.store.units[self.store.indicator.position.y][self.store.indicator.position.x] == 0:
            self.store.screen.display_unit_info(self.store.units[self.store.indicator.position.y][self.store.indicator.position.x].stats)
