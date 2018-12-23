"""
Placeholder
"""

import sys
from random import randint
import pygame

from ..player import Player

class Level():
    def __init__(self, name, players, enemys, terrain, units):
        self.name = name
        self.players = pygame.sprite.Group(players)
        self.enemys = pygame.sprite.Group(enemys)
        self.all_sprites = pygame.sprite.Group(players + enemys)
        self.terrain = terrain
        self.units = units
        self.height = len(units)
        self.width = len(units[0])
        self.enemy_movement_queue = []
        for _player in players:
            self.units[_player.position.y][_player.position.x] = _player
        for _enemy in enemys:
            self.units[_enemy.position.y][_enemy.position.x] = _enemy


    def update_location(self, state, unit):
        self.units[unit.prev_position.y][unit.prev_position.x] = 0
        self.units[unit.position.y][unit.position.x] = unit
        unit.stats.remaining_movement -= 1
        if not unit.stats.remaining_movement:
            unit.image = unit.image_inactive
            state.flags.player_moving = not state.flags.player_moving


    def update_unit_info(self, state):
        if not state.level.units[state.indicator.position.y][state.indicator.position.x] == 0:
            state.screen.display_unit_info(state, state.level.units[state.indicator.position.y][state.indicator.position.x].stats)


    def attack(self, state, attacking_unit, defending_unit):
        if attacking_unit.stats.accuracy - defending_unit.stats.evasion  - self.terrain[defending_unit.position.y][defending_unit.position.x].evasion_adjustment > randint(0, 100):
            defending_unit.stats.current_hp -= attacking_unit.stats.strength - defending_unit.stats.defense - self.terrain[defending_unit.position.y][defending_unit.position.x].def_adjustment
            state.screen.display_context_message("Hit Enemy. Remaining HP: {hp}".format(hp=defending_unit.stats.current_hp))
            self.check_for_unit_death(state, self.units[defending_unit.position.y][defending_unit.position.x])
        else:
            state.screen.display_context_message("Attack Missed!")


    def check_for_unit_death(self, state, unit):
        if unit.stats.current_hp < 1:
            self.units[unit.position.y][unit.position.x] = 0
            self.enemys.remove(unit)
            state.screen.render_terrain(self.terrain[unit.position.y][unit.position.x], unit.position.x, unit.position.y)


    def check_for_turn_end(self, state, units_array):
        unit_with_remaining_movement = False
        for unit in units_array:
            if unit.stats.remaining_movement:
                unit_with_remaining_movement = True
        if not unit_with_remaining_movement:
            self.reset_units_movement(state, units_array)
            state.flags.player_turn = not state.flags.player_turn

        
    def reset_units_movement(self, state, units_array):
        for unit in units_array:
            unit.stats.remaining_movement = int(unit.stats.movement)
            unit.image = unit.image_active
            state.screen.render_unit(unit)
        #TODO: find a better place for this:
        state.screen.render_unit(state.indicator)


    def move_enemy_unit(self, state, unit):
        options = self.unit_to_attack(unit)

        if options:
            self.attack(state, unit, options[0])
        else:
            up = self.is_valid_move(unit.position.x, unit.position.y - 1)
            down = self.is_valid_move(unit.position.x, unit.position.y + 1)
            left = self.is_valid_move(unit.position.x - 1, unit.position.y)
            right = self.is_valid_move(unit.position.x + 1, unit.position.y)

            move = randint(0, 3)
            if move == 0: 
                if up:
                    unit.up()
            elif move == 1:
                if down: 
                    unit.down()
            elif move == 2: 
                if left:
                    unit.left()
            elif move == 3: 
                if right:
                    unit.right()

            prev_terrain = self.terrain[unit.prev_position.y][unit.prev_position.x]
            state.screen.render_terrain(prev_terrain, unit.prev_position.x, unit.prev_position.y)
            state.screen.render_unit(unit)

            self.update_location(state, unit)


    def unit_to_attack(self, unit):
        attack_options= []

        # TODO: Add bounds checking to avoid crashes
        if isinstance(self.units[unit.position.y - 1][unit.position.x], Player):
            attack_options.append(self.units[unit.position.y - 1][unit.position.x])
        elif isinstance(self.units[unit.position.y + 1][unit.position.x], Player):
            attack_options.append(self.units[unit.position.y + 1][unit.position.x])
        elif isinstance(self.units[unit.position.y][unit.position.x - 1], Player):
            attack_options.append(self.units[unit.position.y][unit.position.x - 1])
        elif isinstance(self.units[unit.position.y][unit.position.x + 1], Player):
            attack_options.append(self.units[unit.position.y][unit.position.x + 1])

        return attack_options


    # TODO: Clean this up
    def is_valid_move(self, x, y):
        valid_move = True

        if x < 0 or x > self.height - 1: valid_move = False
        if y < 0 or y > self.width - 1: valid_move = False
        if valid_move:
            if not self.units[y][x] == 0: valid_move = False

        return valid_move


    # TODO: Make some real logic for this
    def enemy_turn(self, state):
        self.reset_units_movement(state, self.enemys)
        for enemy in self.enemys:
            self.move_enemy_unit(state, enemy)


    def check_for_win(self, state):
        if not state.level.enemys:
            state.flags.player_won = True


    def end_game(self, msg):
        print(msg)
        sys.exit()
