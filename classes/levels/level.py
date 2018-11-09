"""
Placeholder
"""

import sys
from random import randint

class Level():
    def __init__(self, name, players, enemys, terrain, units):
        self.name = name
        self.players = players
        self.enemys = enemys
        self.terrain = terrain
        self.units = units
        self.height = len(units)
        self.width = len(units[0])
        for _player in players:
            self.units[_player.position.y][_player.position.x] = _player
        for _enemy in enemys:
            self.units[_enemy.position.y][_enemy.position.x] = _enemy


    # TODO: Deprecate this in favor of below
    def update_unit_location(self, state):
        self.units[state.indicator.position.y][state.indicator.position.x] = self.units[state.indicator.prev_position.y][state.indicator.prev_position.x]
        self.units[state.indicator.prev_position.y][state.indicator.prev_position.x] = 0
        state.flags.player_turn = False

    def update_unit_location_NEW(self, state, unit):
        self.units[unit.prev_position.y][unit.prev_position.x] = 0
        self.units[unit.position.y][unit.position.x] = unit
        state.flags.player_turn = not state.flags.player_turn

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
            self.enemys.pop() # TODO: This is real dirty and should be done better, Also I'm not sure why it works...
            state.screen.render_terrain(self.terrain[unit.position.y][unit.position.x], unit.position.x, unit.position.y)


    def move_unit(self, state, unit):
        unit.update_prev_position()
        prev_terrain = self.terrain[unit.prev_position.y][unit.prev_position.x]

        # TODO: Unit position change decision logic
        move = randint(0, 3)
        if move == 0: unit.position.x += 1
        elif move == 1: unit.position.x -= 1
        elif move == 2: unit.position.y += 1
        elif move == 3: unit.position.y -= 1

        state.screen.render_terrain(prev_terrain, unit.prev_position.x, unit.prev_position.y)
        state.screen.render_unit(unit)

        self.update_unit_location_NEW(state, unit)


    # TODO: Make some real logic for this
    def enemy_turn(self, state):
        max = len(self.enemys)
        index = randint(0, max - 1)
        random_enemy = self.enemys[index]
        self.move_unit(state, random_enemy)


    def check_for_win(self, state):
        if not state.level.enemys:
            state.flags.player_won = True


    def end_game(self, msg):
        print(msg)
        sys.exit()