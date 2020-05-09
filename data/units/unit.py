from random import randint

import pygame as pg

from .. import movement
from ..store import Store
from ..terrain.attackoverlay import AttackOverlay
from ..terrain.moveoverlay import MoveOverlay
from ..tools import image


class Unit(pg.sprite.Sprite):
    def __init__(self, init_pos_tuple, info):
        pg.sprite.Sprite.__init__(self)

        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)

        self.stats = Stats(info["stats"])

        # TODO: Clean up the clean up attempt
        self.images = Images(info)
        self.image = self.images.image
        self.active = False
        self.store = Store.instance()

    def update(self):
        if self.active:
            self.idle_animation()

    ######################
    # Movement functions #
    ######################

    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)

    def update_location(self):
        self.store.units[self.prev_position.y][self.prev_position.x] = 0
        self.store.units[self.position.y][self.position.x] = self

    def move_to_position(self, new_pos):
        self.update_prev_position()
        self.position.y = int(new_pos.y)
        self.position.x = int(new_pos.x)
        self.update_location()

    # TODO: Hardcoding is bad
    # TODO: Clean up highlights on state shift

    def setup_movement_highlight(self):
        valid_movements = movement.bfs(
            # TODO: fix magic numbers
            (self.position.x, self.position.y), self.stats.movement, 0, 9
        )
        print('valid movement', valid_movements)

        move_overlay = MoveOverlay()
        for mov in valid_movements:
            self.store.highlights[mov[1]][mov[0]] = move_overlay
            self.store.screen.render_square(mov[0], mov[1])

        # Attack overlay
        valid_attacks = movement.bfs(
            # TODO: fix magic numbers
            (self.position.x, self.position.y),
            self.stats.movement + self.stats.max_attack_range, 0, 9
        )
        print('valid attacks', valid_attacks)
        unique = set(valid_attacks) - set(valid_movements)
        attack_overlay = AttackOverlay()
        for mov in unique:
            self.store.highlights[mov[1]][mov[0]] = attack_overlay
            self.store.screen.render_square(mov[0], mov[1])

        return valid_attacks

    def cleanup_movement_highlights(self):
        for y in range(len(self.store.highlights)):
            for x in range(len(self.store.highlights[0])):
                if self.store.highlights[y][x]:
                    self.store.screen.display.blit(
                        self.store.highlights[y][x].image, (x * 32, y * 32))

    def cleanup_attack_highlights(self):
        for y in range(len(self.store.highlights)):
            for x in range(len(self.store.highlights[0])):
                if self.store.highlights[y][x]:
                    self.store.highlights[y][x] = 0
                    self.store.screen.render_square(x, y)

    def update_pre_pos(self, val):
        print('testing prepos')
        if val == 'x':
            pre_pos = self.store.paired_unit.position.x
            print(val, pre_pos)
            return pre_pos
        elif val == 'y':
            pre_pos = self.store.paired_unit.position.y
            print(val, pre_pos)
            return pre_pos

    ####################
    # Attack Functions #
    ####################

    def attack(self, defending_unit) -> None:
        if self.chance_to_hit(defending_unit) > self.attack_roll():
            attack_damage = self.attack_damage(defending_unit)
            defending_unit.stats.current_hp -= attack_damage
            self.store.screen.display_context_message(
                f"Hit Enemy for {attack_damage}. Remaining HP: {defending_unit.stats.current_hp}"
            )
            defending_unit.check_for_death()
        else:
            self.store.screen.display_context_message("Attack Missed!")

    def attack_damage(self, defending_unit) -> int:
        strength = self.stats.strength
        defense = defending_unit.stats.defense
        terrain_adjustment = self.store.terrain[defending_unit.position.y][defending_unit.position.x].def_adjustment
        damage = strength - defense - terrain_adjustment

        if damage > 0:
            return damage
        else:
            return 0

    def attack_roll(self) -> int:
        return randint(0, 100)

    def chance_to_hit(self, defending_unit) -> int:
        accuracy = self.stats.accuracy
        evasion = defending_unit.stats.evasion
        terrain_adjustment = self.store.terrain[defending_unit.position.y][
            defending_unit.position.x].evasion_adjustment

        return accuracy - evasion - terrain_adjustment

    def display_attack_overlay(self):
        attack_overlay = AttackOverlay()

        inner = movement.bfs((self.position.x, self.position.y),
                             self.stats.min_attack_range - 1, 0, 9)
        outer = movement.bfs((self.position.x, self.position.y),
                             self.stats.max_attack_range, 0, 9)
        difference = set(outer) - set(inner)

        for mov in difference:
            self.store.highlights[mov[1]][mov[0]] = attack_overlay
            self.store.screen.render_square(mov[0], mov[1])

    ####################################
    # Remaing Functions (Alphabetical) #
    ####################################

    # TODO: Alter idle animations to allow more than one frame

    def idle_animation(self):
        if self.images.is_idle_1:
            self.image = self.images.idle_2
        else:
            self.image = self.images.idle_1

        self.images.is_idle_1 = not self.images.is_idle_1
        self.store.screen.render_terrain(self.position.x, self.position.y)
        self.store.screen.render_unit(self.position.x, self.position.y)

    def check_for_death(self):
        if self.stats.current_hp <= 0:
            print('Dead')
            self.store.units[self.position.y][self.position.x] = 0
            self.store.screen.render_square(self.position.x, self.position.y)
            # TODO: Look for cleaner way to do this, a conditional based on a flag on the unit should be quicker than iterating through an extra list
            self.store.enemys.remove(self)
            self.store.players.remove(self)
            self.store.all_units.remove(self)


##################
# Helper Classes #
##################

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
        # TODO: Obsolete remove
        self.remaining_movement = init_stats["movement"]
        self.min_attack_range = init_stats["min_attack_range"]
        self.max_attack_range = init_stats["max_attack_range"]


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1]


class Images():
    def __init__(self, info):
        self.is_idle_1 = True
        self.idle_1 = image.load_png(info["idle_1_path"])
        self.idle_2 = image.load_png(info["idle_2_path"])

        self.image = self.idle_1
