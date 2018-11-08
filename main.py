"""
Placeholder
"""

import pygame

from classes.enemy import Enemy
from classes.player import Player
from classes.indicator import Indicator
from classes.state import State
from classes.screen import Screen
from classes.levels.intro import Intro
from classes.event_handler import EventHandler

pygame.init()
state = State(Screen(), Intro(), Indicator((0, 0)))
event_handler = EventHandler()

state.screen.init_screen(state.level.terrain)
state.screen.init_info_pane(state)
state.screen.init_context_menu()
state.screen.display_terrain_info(state)

state.screen.render_unit(state.indicator)

for _player in state.level.players:
    state.screen.render_unit(_player)

for _enemy in state.level.enemys:
    state.screen.render_unit(_enemy)

pygame.display.update()

while 1:
    if state.flags.player_won:
        state.level.end_game('You Win')

    state.flags.update = False

    for event in pygame.event.get():
        event_handler.handle(event, state)

    if state.flags.update:
        state.level.check_for_win(state)
        state.screen.clear_info_pane(state)
        state.screen.move_indicator(state)
        state.level.update_unit_info(state)
        state.screen.display_terrain_info(state)
        pygame.display.update()
