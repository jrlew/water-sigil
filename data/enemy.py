"""
Placeholder
"""

import pygame
from .units.unit import Unit
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
