import pygame as pg
from .state import State
from ..player import Player

# TODO: Find a better name for this
# Phase for Non-Paired Indicator
class PlayerPhase(State):
    def __init__(self):
        super(PlayerPhase, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):
        print('Player Phase Beginning')
        self.persist = persistent

        for unit in self.persist.players:
            if unit.stats.remaining_movement:
                unit.active = True
            else:
                unit.active = False
        for unit in self.persist.enemys:
            unit.active = False

        playerTurn = False
        for player in self.persist.players:
            if player.stats.remaining_movement > 0:
                playerTurn = True

        if not playerTurn:
            print("Player Turn should end now")
            self.done = True
            self.next_state = "EnemyPhase"

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
            elif event.key == pg.K_RETURN:
                if isinstance(self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x], Player):
                    self.persist.paired_unit = self.persist.units[self.persist.indicator.position.y][self.persist.indicator.position.x]
                    print(self.persist.paired_unit.stats.name)
                    self.done = True
                    self.next_state = "UnitPhase"

    def update(self, dt):
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
