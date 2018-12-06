"""
Placeholder
"""

import pygame as pg
from random import randint
from ..tools import image
from ..terrain.attackoverlay import AttackOverlay

class Unit(pg.sprite.Sprite):
    def __init__(self, init_pos_tuple, info):
        pg.sprite.Sprite.__init__(self)

        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)

        self.stats = Stats(info["stats"])

        # TODO: Clean up the clean up attempt
        self.images = Images(info)
        self.image = self.images.image

        # self.image_active = image.load_png(info["image_active_path"])
        # self.image_inactive = image.load_png(info["image_inactive_path"])
        # self.image = self.image_active
        # self.is_idle_1 = True
        # self.idle_1 = image.load_png(info["idle_1_path"])
        # self.idle_2 = image.load_png(info["idle_2_path"])
        # self.rect = self.image.get_rect()


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


    def display_attack_overlay(self, persist):
        attack_overlay = AttackOverlay()
        persist.highlights[self.position.y - 1][self.position.x] = attack_overlay
        persist.highlights[self.position.y + 1][self.position.x] = attack_overlay
        persist.highlights[self.position.y][self.position.x - 1] = attack_overlay
        persist.highlights[self.position.y][self.position.x + 1] = attack_overlay


    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)


    def update(self, persist):
        self.idle_animation(persist)

    
    # TODO: This should probably be a tempt location
    def update_unit_location(self, units):
        units[self.prev_position.y][self.prev_position.x] = 0
        units[self.position.y][self.position.x] = self
        self.stats.remaining_movement -= 1


    # TODO: This probably shoudn't be here or image class property should move (it works but using property that only exist on classes that use this seems dangerous)
    def idle_animation(self, persist):
        if self.images.is_idle_1:
            self.image = self.images.idle_2
        else:
            self.image = self.images.idle_1

        self.images.is_idle_1 = not self.images.is_idle_1
        persist.screen.render_terrain(persist.terrain[self.position.y][self.position.x], self.position.x, self.position.y)
        persist.screen.render_unit(self)


    def attack(self, persist, defending_unit):
        if self.stats.accuracy - defending_unit.stats.evasion  - persist.terrain[defending_unit.position.y][defending_unit.position.x].evasion_adjustment > randint(0, 100):
            defending_unit.stats.current_hp -= self.stats.strength - defending_unit.stats.defense - persist.terrain[defending_unit.position.y][defending_unit.position.x].def_adjustment
            persist.screen.display_context_message("Hit Enemy. Remaining HP: {hp}".format(hp=defending_unit.stats.current_hp))
            defending_unit.check_for_death(persist)
        else:
            persist.screen.display_context_message("Attack Missed!")

    
    # TODO: Finish figure out how to remove unit from enemys/players/all_units
    def check_for_death(self, persist):
        if self.stats.current_hp <= 0:
            print('Dead')
            persist.units[self.position.y][self.position.x] = 0
            persist.screen.render_square(persist, self.position.x, self.position.y)


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


class Images():
    def __init__(self, info):
        self.image_active = image.load_png(info["image_active_path"])
        self.image_inactive = image.load_png(info["image_inactive_path"])

        self.image = self.image_active

        self.is_idle_1 = True
        self.idle_1 = image.load_png(info["idle_1_path"])
        self.idle_2 = image.load_png(info["idle_2_path"])
    
