"""
Placeholder
"""

import pygame
from ..tools import image

class Unit(pygame.sprite.Sprite):
    def __init__(self, init_pos_tuple, info):
        pygame.sprite.Sprite.__init__(self)

        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)

        self.stats = Stats(info["stats"])

        self.image_active = image.load_png(info["image_active_path"])
        self.image_inactive = image.load_png(info["image_inactive_path"])
        self.image = self.image_active
        self.is_idle_1 = True
        self.idle_1 = image.load_png(info["idle_1_path"])
        self.idle_2 = image.load_png(info["idle_2_path"])
        self.rect = self.image.get_rect()


    def up(self, units):
        self.update_prev_position()
        self.position.y -= 1
        self.update_unit_location(units)


    def down(self, units):
        self.update_prev_position()
        self.position.y += 1
        self.update_unit_location(units)


    def left(self, units):
        self.update_prev_position()
        self.position.x -= 1
        self.update_unit_location(units)


    def right(self, units):
        self.update_prev_position()
        self.position.x += 1
        self.update_unit_location(units)


    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)


    def update(self, state):
        self.idle_animation(state)

    
    # TODO: This should probably be a tempt location
    def update_unit_location(self, units):
        units[self.prev_position.y][self.prev_position.x] = 0
        units[self.position.y][self.position.x] = self
        self.stats.remaining_movement -= 1
        # TODO: Reempliment movement subtraction
        # TODO: Add check in movement phase to block movement after emptied
        # if not unit.stats.remaining_movement:
        #     unit.image = unit.image_inactive
        #     state.flags.player_moving = not state.flags.player_moving


    # TODO: This probably shoudn't be here or image class property should move (it works but using property that only exist on classes that use this seems dangerous)
    def idle_animation(self, state):
        if self.is_idle_1:
                self.image = self.idle_2
        else:
                self.image = self.idle_1
        self.is_idle_1 = not self.is_idle_1
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
