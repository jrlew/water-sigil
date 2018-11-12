"""
Placeholder
"""

import pygame

class Unit():
    def __init__(self, init_pos_tuple, stats_dict):
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.stats = Stats(stats_dict)

    def up(self):
        self.update_prev_position()
        self.position.y -= 1

    def down(self):
        self.update_prev_position()
        self.position.y += 1

    def left(self):
        self.update_prev_position()
        self.position.x -= 1

    def right(self):
        self.update_prev_position()
        self.position.x += 1

    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)

    # TODO: This probably shoudn't be here or image class property should move (it works but using property that only exist on classes that use this seems dangerous)
    def idle_animation(self, state):
        self.image = pygame.transform.flip(self.image, 1, 0)
        state.screen.render_terrain(state.level.terrain[self.position.y][self.position.x], self.position.x, self.position.y)
        state.screen.render_unit(self)


class Stats():
    def __init__(self, init_stats):
        self.name = init_stats["name"]
        self.max_hp = init_stats["hp"]
        self.current_hp = init_stats["hp"]
        self.strength = init_stats["strength"]
        self.defense = init_stats["defense"]
        self.accuracy = init_stats["accuracy"]
        self.evasion = init_stats["evasion"]
        self.movement = init_stats["movement"]
        self.remaining_movement = init_stats["movement"]


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1] 
