"""
Placeholder
"""

import pygame

from data.enemy import Enemy
from data.player import Player
from data.indicator import Indicator
from data.state import State
from data.screen import Screen
from data.levels.intro import Intro
from data.event_handler import EventHandler
from data.utils import audio

pygame.init()
state = State(Screen(), Intro(), Indicator((0, 0)))
event_handler = EventHandler()
clock = pygame.time.Clock()
FPS = 30

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

# TODO: Audio load/play should probably be handled in the level file
# main_theme = audio.load_sound("audio/beepbox-poc.wav")
# main_theme.play(-1)

# Event to prompt updating to the next frame of units idle animation
pygame.time.set_timer(event_handler.custom_events.UPDATE_ANIMATION, 650)

while 1:
    clock.tick(FPS)
    # TODO: Now that updating the display on every frame has been decided. Clear out all other pygame.display.update()s from the code
    pygame.display.update() 

    if state.flags.player_won:
        state.level.end_game('You Win')

    state.flags.update = False

    if state.flags.player_turn:
        # TODO: Move current turn message to some other part of the UI
        # state.screen.display_context_message("Player Turn")
        
        for event in pygame.event.get():
            event_handler.handle(event, state)

        if state.flags.update:
            state.level.check_for_win(state)
            state.screen.clear_info_pane(state)
            state.screen.move_indicator(state)
            state.level.update_unit_info(state)
            state.screen.display_terrain_info(state)

            # TODO: this should check on movement not on every cyle...
            state.level.check_for_turn_end(state, state.level.players)

    else:
        # TODO: Move current turn message to some other part of the UI
        # state.screen.display_context_message("Enemy Turn")
        state.level.enemy_turn(state)
        state.level.reset_units_movement(state, state.level.enemys)
        state.flags.player_turn = not state.flags.player_turn
