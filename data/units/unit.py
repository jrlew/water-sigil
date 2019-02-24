"""
Placeholder
"""

import pygame as pg
from random import randint
from ..tools import image
from ..terrain.attackoverlay import AttackOverlay
from ..terrain.moveoverlay import MoveOverlay
from .. import movement

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


    def update(self, persist):
        if self.active:
            self.idle_animation(persist)


    ######################
    # Movement functions #
    ######################

    def up(self, persist):
        self.update_prev_position()
        self.position.y -= 1
        self.update_location(persist)


    def down(self, persist):
        self.update_prev_position()
        self.position.y += 1
        self.update_location(persist)


    def left(self, persist):
        self.update_prev_position()
        self.position.x -= 1
        self.update_location(persist)


    def right(self, persist):
        self.update_prev_position()
        self.position.x += 1
        self.update_location(persist)


    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)

    
    def update_location(self, persist):
        persist.units[self.prev_position.y][self.prev_position.x] = 0
        persist.units[self.position.y][self.position.x] = self
        self.stats.remaining_movement -= 1


    def move_to_position(self, persist, new_pos):
        self.update_prev_position()
        self.position.y = int(new_pos.y)
        self.position.x = int(new_pos.x)
        self.update_location(persist)
        

    # TODO: Hardcoding is bad
    # TODO: Clean up highlights on state shift
    def setup_movement_highlight(self, persist):
        valid_movements = movement.bfs(persist, (self.position.x, self.position.y), self.stats.movement, 0, 9) # TODO: fix magic numbers

        move_overlay = MoveOverlay()
        for mov in valid_movements:
            persist.highlights[mov[1]][mov[0]] = move_overlay
            persist.screen.render_square(persist, mov[0], mov[1])

        # Attack overlay
        valid_attacks = movement.bfs(persist, (self.position.x, self.position.y), self.stats.movement + self.stats.max_attack_range, 0, 9) # TODO: fix magic numbers
        unique = set(valid_attacks) - set(valid_movements)
        attack_overlay = AttackOverlay()
        for mov in unique:
            persist.highlights[mov[1]][mov[0]] = attack_overlay
            persist.screen.render_square(persist, mov[0], mov[1])
        
        return valid_attacks

    def cleanup_movement_highlights(self, persist):
        for y in range(len(persist.highlights)):
            for x in range(len(persist.highlights[0])):
                if persist.highlights[y][x]:
                    print("howdy")
                    persist.screen.display.blit(persist.highlights[y][x].image, (x  * 32, y * 32))

    def cleanup_attak_highlights(self, persist):
        for y in range(len(persist.highlights)):
            for x in range(len(persist.highlights[0])):
                if persist.highlights[y][x]:
                    persist.highlights[y][x] = 0
                    persist.screen.render_square(persist, x, y)


    ####################
    # Attack Functions #
    ####################

    def attack(self, persist, defending_unit):
        if self.stats.accuracy - defending_unit.stats.evasion  - persist.terrain[defending_unit.position.y][defending_unit.position.x].evasion_adjustment > randint(0, 100):
            defending_unit.stats.current_hp -= self.stats.strength - defending_unit.stats.defense - persist.terrain[defending_unit.position.y][defending_unit.position.x].def_adjustment
            persist.screen.display_context_message("Hit Enemy. Remaining HP: {hp}".format(hp=defending_unit.stats.current_hp))
            defending_unit.check_for_death(persist)
        else:
            persist.screen.display_context_message("Attack Missed!")


    def display_attack_overlay(self, persist):
        attack_overlay = AttackOverlay()

        inner = movement.bfs(persist, (self.position.x, self.position.y), self.stats.min_attack_range - 1, 0, 9)
        outer = movement.bfs(persist, (self.position.x, self.position.y), self.stats.max_attack_range, 0, 9)
        difference = set(outer) - set(inner)

        for mov in difference:
            persist.highlights[mov[1]][mov[0]] = attack_overlay
            persist.screen.render_square(persist, mov[0], mov[1])        


    ####################################
    # Remaing Functions (Alphabetical) #
    ####################################

    # TODO: Alter idle animations to allow more than one frame
    def idle_animation(self, persist):
        if self.images.is_idle_1:
            self.image = self.images.idle_2
        else:
            self.image = self.images.idle_1

        self.images.is_idle_1 = not self.images.is_idle_1
        persist.screen.render_terrain(persist, self.position.x, self.position.y)
        persist.screen.render_unit(persist, self.position.x, self.position.y)

    
    def check_for_death(self, persist):
        if self.stats.current_hp <= 0:
            print('Dead')
            persist.units[self.position.y][self.position.x] = 0
            persist.screen.render_square(persist, self.position.x, self.position.y)
            # TODO: Look for cleaner way to do this, a conditional based on a flag on the unit should be quicker than iterating through an extra list
            persist.enemys.remove(self)
            persist.players.remove(self)
            persist.all_units.remove(self)
            

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
        self.remaining_movement = init_stats["movement"] # TODO: Obsolete remove
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
    
