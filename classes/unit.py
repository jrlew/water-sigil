"""
Placeholder
"""

import pygame


class Unit(pygame.sprite.Sprite):
    def __init__(self, init_pos_tuple, _is_player):
        # pygame.sprite.Sprite()
        self.is_player = _is_player
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.stats = Stats()

    def up(self):
        self.update_prev_position()
        self.position.y += -1

    def down(self):
        self.update_prev_position()
        self.position.y += 1

    def left(self):
        self.update_prev_position()
        self.position.x += -1

    def right(self):
        self.update_prev_position()
        self.position.x += 1

    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)


class Stats():
    def __init__(self):
        self.max_hp = 20
        self.current_hp = 18
        self.strength = 6
        self.defense = 3


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1] 
