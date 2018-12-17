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
        self.squares_to_cleanup = []


    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        print("Unit Phase Beginning")
        self.persist = persistent
        # TODO: Name this better and maybe make it a part of persist
        self.squares_to_cleanup = self.persist.paired_unit.setup_movement_highlight(self.persist)


    # TODO: Change this to move player on 'enter' when indicator is on highlighted square
    def get_event(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.persist.indicator.up()
                self.persist.paired_unit.up(self.persist)
            elif event.key == pg.K_DOWN:
                self.persist.indicator.down()
                self.persist.paired_unit.down(self.persist)
            elif event.key == pg.K_RIGHT:
                self.persist.indicator.right()
                self.persist.paired_unit.right(self.persist)
            elif event.key == pg.K_LEFT:
                self.persist.indicator.left()
                self.persist.paired_unit.left(self.persist)


    def update(self, dt):
        # TODO: Scrap this when movement changed
        if self.persist.paired_unit.stats.remaining_movement == 0:
            print("Change state")
            self.done = True
            self.next_state = "UnitAttackPhase"
            # TODO: Move this into a function somewhere
            for mov in self.squares_to_cleanup:
                self.persist.highlights[mov[1]][mov[0]] = 0
                self.persist.screen.render_square(self.persist, mov[0], mov[1])


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
