import pygame as pg

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
        self.persist = {}
        self.font = pg.font.Font(None, 24)


    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        print("Unit Phase Beginning")
        self.persist = persistent
        # TODO: Name this better and maybe make it a part of persist
        self.persist.current_highlights = self.persist.paired_unit.setup_movement_highlight(self.persist)


    # TODO: Change this to move player on 'enter' when indicator is on highlighted square
    def get_event(self, event):
        pre_pos_x = self.persist.paired_unit.update_pre_pos(self.persist, 'x')
        pre_pos_y = self.persist.paired_unit.update_pre_pos(self.persist, 'y')
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist.indicator.up() 
            elif event.key == pg.K_DOWN:
                self.persist.indicator.down()
            elif event.key == pg.K_RIGHT:
                self.persist.indicator.right()
            elif event.key == pg.K_LEFT:
                self.persist.indicator.left()
            elif event.key == pg.K_RETURN:
                if isinstance(self.persist.highlights[self.persist.indicator.position.y][self.persist.indicator.position.x], MoveOverlay) and not self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x]:
                    print("Change state")
                    self.done = True
                    self.next_state = "UnitAttackPhase"
                    self.persist.paired_unit.move_to_position(self.persist, self.persist.indicator.position)
                    for mov in self.persist.current_highlights:
                        self.persist.highlights[mov[1]][mov[0]] = 0
                        self.persist.screen.render_square(self.persist, mov[0], mov[1])
                elif self.persist.paired_unit.position.x == self.persist.indicator.position.x and self.persist.paired_unit.position.y == self.persist.indicator.position.y:
                    print("Ending Turn No Movement")
                    self.done = True
                    self.next_state = "UnitAttackPhase"
                    for mov in self.persist.current_highlights:
                        self.persist.highlights[mov[1]][mov[0]] = 0
                        self.persist.screen.render_square(self.persist, mov[0], mov[1])
                else:
                    self.persist.screen.display_context_message("Unable To Move Units To Selected Tile")
            elif event.key == pg.K_ESCAPE:
                print("backout completed")
                for mov in self.persist.current_highlights:
                        self.persist.highlights[mov[1]][mov[0]] = 0
                        self.persist.screen.render_square(self.persist, mov[0], mov[1])
                self.persist.paired_unit.cleanup_movement_highlights(self.persist)
                self.done = True
                self.next_state = "Player_Phase"
                
                


    def update(self, dt):
        pass


    def draw(self, screen):
        # TODO: Don't draw every tick.... somehow
        # Resetting old square and setting up new square
        screen.render_square(self.persist, self.persist.indicator.prev_position.x, self.persist.indicator.prev_position.y)
        screen.render_square(self.persist, self.persist.indicator.position.x, self.persist.indicator.position.y)

        # Clear old info and setup new
        screen.clear_info_pane()
        screen.display_terrain_info(self.persist.terrain[self.persist.indicator.position.y][self.persist.indicator.position.x])
        if not self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x] == 0:
            screen.display_unit_info(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x].stats)
