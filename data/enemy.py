"""
Placeholder
"""

import pygame
from .units.unit import Unit, Position
from .movement import bfs
from .player import Player

class Enemy(Unit):
    def __init__(self, init_pos, job):
        Unit.__init__(self, init_pos, job.info)


    def move_towards_player(self, persist):
        possible = bfs(persist, (self.position.x, self.position.y), self.stats.movement + self.stats.max_attack_range, 0, 10)
        for entry in possible:
            if isinstance(persist.units[entry[1]][entry[0]], Player):
                print('Gottem', entry)
                move_to = self.find_adjacent_square((self.position.x, self.position.y), entry)
                self.move_to_position(persist, Position(move_to))
                # persist.screen.render_square(persist, self.prev_position.x, self.prev_position.y)
                break


    def find_adjacent_square(self, init, goal):
        print('goal: ', goal)
        move = [0, 0]
        if init[0] > goal[0]:
            move[0] = goal[0] + 1
        elif init[0] < goal[0]:
            move[0] = goal[0] - 1
        elif init[0] == goal[0]:
            move[0] = goal[0]

        if init[1] > goal[1]:
            move[1] = goal[1] + 1
        elif init [1] < goal[1]:
            move[1] = goal[1] - 1
        elif init[1] == goal[1]:
            move[1] = goal[1]
        print('finding: ', init, ' - ', goal, ' - ', move)
        return move