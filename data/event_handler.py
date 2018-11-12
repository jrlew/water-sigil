"""
Placeholder
"""

import pygame

from .player import Player
from .enemy import Enemy


class EventHandler():
    def __init__(self):
        self.placholder = True
        self.custom_events = CustomEvents()

    def handle(self, event, state):
        if event.type == pygame.QUIT:
            state.level.end_game('Game Over')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up_key_handler(state)
            elif event.key == pygame.K_DOWN:
                self.down_key_handler(state)
            elif event.key == pygame.K_RIGHT:
                self.right_key_handler(state)
            elif event.key == pygame.K_LEFT:
                self.left_key_handler(state)
            elif event.key == pygame.K_RETURN:
                self.enter_key_handler(state)
        elif event.type == self.custom_events.UPDATE_ANIMATION:
                self.update_animation_handler(state)


    def up_key_handler(self, state):
        if not state.indicator.position.y - 1 < 0:
            if state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y - 1][state.indicator.position.x], Enemy):
                state.level.attack(state, state.level.units[state.indicator.position.y][state.indicator.position.x], state.level.units[state.indicator.position.y - 1][state.indicator.position.x])
                state.flags.update = True
            elif state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y - 1][state.indicator.position.x], Player):
                pass
            else:
                state.indicator.up()
                state.flags.update = True
                if state.flags.player_moving:
                    state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x].up()
                    state.level.update_unit_location(state, state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x])


    def down_key_handler(self, state):
        if not state.indicator.position.y + 1 > (state.level.height - 1):
            if state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y + 1][state.indicator.position.x], Enemy):
                state.level.attack(state, state.level.units[state.indicator.position.y][state.indicator.position.x], state.level.units[state.indicator.position.y + 1][state.indicator.position.x])
                state.flags.update = True
            elif state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y + 1][state.indicator.position.x], Player):
                pass
            else:
                state.indicator.down()
                state.flags.update = True
                if state.flags.player_moving:
                    state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x].down()
                    state.level.update_unit_location(state, state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x])


    def right_key_handler(self, state):
        if not state.indicator.position.x + 1 > (state.level.width - 1):
            if state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y][state.indicator.position.x + 1], Enemy):
                state.level.attack(state, state.level.units[state.indicator.position.y][state.indicator.position.x], state.level.units[state.indicator.position.y][state.indicator.position.x + 1])
                state.flags.update = True
            elif state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y][state.indicator.position.x + 1], Player):
                pass
            else:
                state.indicator.right()
                state.flags.update = True
                if state.flags.player_moving:
                    state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x].right()
                    state.level.update_unit_location(state, state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x])


    def left_key_handler(self, state):
        if not state.indicator.position.x - 1 < 0:
            if state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y][state.indicator.position.x - 1], Enemy):
                state.level.attack(state, state.level.units[state.indicator.position.y][state.indicator.position.x], state.level.units[state.indicator.position.y][state.indicator.position.x - 1])
                state.flags.update = True
            elif state.flags.player_moving and isinstance(state.level.units[state.indicator.position.y][state.indicator.position.x - 1], Player):
                pass
            else:
                state.indicator.left()
                state.flags.update = True
                if state.flags.player_moving:
                    state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x].left()
                    state.level.update_unit_location(state, state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x])


    def enter_key_handler(self, state):
        if state.flags.player_moving:
            state.flags.player_moving = False
        else:
            if isinstance(state.level.units[state.indicator.position.y][state.indicator.position.x], Player):
                if state.level.units[state.indicator.position.y][state.indicator.position.x].stats.remaining_movement:
                    state.flags.player_moving = True


    def update_animation_handler(self, state):
        # TODO: Add pygame.sprite.Sprite to unit class
        # TODO: Add players and enemys to sprite groups
        # TODO: Call update on AllSprites group instead of manually looping through them
        for player in state.level.players:
            player.idle_animation(state)
        for enemy in state.level.enemys:
            enemy.idle_animation(state)
        state.screen.render_unit(state.indicator)
        pygame.display.update()

class CustomEvents():
    def __init__(self):
        self.UPDATE_ANIMATION = pygame.USEREVENT + 1