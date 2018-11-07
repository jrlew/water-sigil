"""
Placeholder
"""

import sys
from random import randint
import pygame

from classes.enemy import Enemy
from classes.player import Player
from classes.indicator import Indicator
from classes.state import State
from classes.levels.intro import Intro

# Everything Pygame related has be below this line
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
size = width, height = 480, 360
PIXEL_SIZE = 32
FONT_SIZE = 24
MSG_WIDTH = 150
MSG_HEIGHT = 120

screen = pygame.display.set_mode(size)
state = State()
level = Intro()

indicator = Indicator((0, 0))

FONT = pygame.font.Font(None, FONT_SIZE)

UNITS_LEN = len(level.units[0])
INFO_PANE_X_OFFSET = UNITS_LEN * PIXEL_SIZE

def init_screen(map_array):
    y_coord = 0
    for row in map_array:
        x_coord = 0
        for col in row:
            screen.blit(col.image, (x_coord, y_coord))
            x_coord += PIXEL_SIZE
        y_coord += PIXEL_SIZE


def render_unit(unit):
    screen.blit(unit.image, (unit.position.x * PIXEL_SIZE, unit.position.y * PIXEL_SIZE))


def render_terrain(terrain, x_coord, y_coord):
    screen.blit(terrain.image, (x_coord * PIXEL_SIZE, y_coord * PIXEL_SIZE))


def move_indicator():
    render_terrain(level.terrain[indicator.prev_position.y][indicator.prev_position.x], indicator.prev_position.x, indicator.prev_position.y)
    if not level.units[indicator.prev_position.y][indicator.prev_position.x] == 0:
        render_unit(level.units[indicator.prev_position.y][indicator.prev_position.x])

    render_terrain(level.terrain[indicator.position.y][indicator.position.x], indicator.position.x, indicator.position.y)
    if not level.units[indicator.position.y][indicator.position.x] == 0:
        render_unit(level.units[indicator.position.y][indicator.position.x])

    render_unit(indicator)


def update_unit_location():
    level.units[indicator.position.y][indicator.position.x] = level.units[indicator.prev_position.y][indicator.prev_position.x]
    level.units[indicator.prev_position.y][indicator.prev_position.x] = 0


def init_info_pane():
    # Horizontal Bars for Unit Info
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 0, 160, 4], 0)
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 29, 160, 4], 0)

    # Horizontal Dividing Bar
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 157, 160, 4], 0)

    # Horizontal Bars for Terrain Info
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 190, 160, 4], 0)
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 315, 160, 4], 0)

    # Vertical Bars
    pygame.draw.rect(screen, WHITE, [INFO_PANE_X_OFFSET, 0, 4, 320], 0)
    pygame.draw.rect(screen, WHITE, [width - 5, 0, 4, 320], 0)

    # Text
    screen.blit(FONT.render("UNIT INFO", 1, (200, 200, 200)), (INFO_PANE_X_OFFSET + 8, 6))
    screen.blit(FONT.render("TERRAIN INFO", 1, (200, 200, 200)), (INFO_PANE_X_OFFSET + 8, 165))

    # Bottom Context Message
    # TODO: Doesn't make sense for this function, fix name or move this
    pygame.draw.rect(screen, WHITE, [0, 320, width, 4], 0)
    pygame.draw.rect(screen, WHITE, [0, 355, width, 4], 0)

    pygame.draw.rect(screen, WHITE, [0, 320, 4, 40], 0)
    pygame.draw.rect(screen, WHITE, [475, 320, 4, 40], 0)


def display_unit_info(stats):
    info = [
        "{name}".format(name=stats.name),
        "HP: {hp} / {maxhp}".format(hp=stats.current_hp, maxhp=stats.max_hp),
        "STR: {str}  DEF: {defense}".format(str=stats.strength, defense=stats.defense),
        "ACC: {acc}  EVD: {evd}".format(acc=stats.accuracy, evd=stats.evasion),
    ]
    y_offset = 34
    for line in info:
        screen.blit(FONT.render(line, 1, (200, 200, 200)), (INFO_PANE_X_OFFSET + 8, y_offset))
        y_offset += (FONT_SIZE + 4)


def clear_info_pane():
    pygame.draw.rect(screen, BLACK, [INFO_PANE_X_OFFSET + 4, 34, MSG_WIDTH, MSG_HEIGHT], 0)
    pygame.draw.rect(screen, BLACK, [INFO_PANE_X_OFFSET + 4, 195, MSG_WIDTH, MSG_HEIGHT], 0)


def display_terrain_info():
    ter = level.terrain[indicator.position.y][indicator.position.x]
    terrain_info = [
        "{type}".format(type=ter.type),
        "Def: {def_adjustment}".format(def_adjustment=ter.def_adjustment),
        "Evd: {evasion_adjustment}".format(evasion_adjustment=ter.evasion_adjustment),
    ]
    y_offset = 195
    for line in terrain_info:
        screen.blit(FONT.render(line, 1, (200, 200, 200)), (INFO_PANE_X_OFFSET + 8, y_offset))
        y_offset += (FONT_SIZE + 4)


def update_unit_info():
    if not level.units[indicator.position.y][indicator.position.x] == 0:
        display_unit_info(level.units[indicator.position.y][indicator.position.x].stats)


def display_context_message(msg_text):
    pygame.draw.rect(screen, BLACK, [8, 329, 440, 26], 0)
    screen.blit(FONT.render(msg_text, 1, (200, 200, 200)), (8, 329))


# TODO: This is pretty gross
def check_for_unit_death(unit):
    if unit.stats.current_hp < 1:
        level.units[unit.position.y][unit.position.x] = 0
        level.enemys.pop() # TODO: This is real dirty and should be done better
        screen.blit(level.terrain[unit.position.y][unit.position.x].image, (unit.position.x * PIXEL_SIZE, unit.position.y * PIXEL_SIZE))


def attack(attacking_unit, defending_unit):
    if attacking_unit.stats.accuracy - defending_unit.stats.evasion  - level.terrain[defending_unit.position.y][defending_unit.position.x].evasion_adjustment > randint(0, 100):
        defending_unit.stats.current_hp -= attacking_unit.stats.strength - defending_unit.stats.defense
        display_context_message("Hit Enemy. Remaining HP: {hp}".format(hp=defending_unit.stats.current_hp))
        check_for_unit_death(level.units[defending_unit.position.y][defending_unit.position.x])
    else:
        display_context_message("Attack Missed!")


def up_key_handler():
    if not indicator.position.y - 1 < 0:
        if state.player_moving_flag and isinstance(level.units[indicator.position.y - 1][indicator.position.x], Enemy):
            attack(level.units[indicator.position.y][indicator.position.x], level.units[indicator.position.y - 1][indicator.position.x])
            state.update_flag = True
        elif state.player_moving_flag and isinstance(level.units[indicator.position.y - 1][indicator.position.x], Player):
            pass
        else:
            indicator.up()
            state.update_flag = True
            if state.player_moving_flag:
                level.units[indicator.prev_position.y][indicator.prev_position.x].up()
                update_unit_location()


def down_key_handler():
    if not indicator.position.y + 1 > (UNITS_LEN - 1):
        if state.player_moving_flag and isinstance(level.units[indicator.position.y + 1][indicator.position.x], Enemy):
            attack(level.units[indicator.position.y][indicator.position.x], level.units[indicator.position.y + 1][indicator.position.x])
            state.update_flag = True
        elif state.player_moving_flag and isinstance(level.units[indicator.position.y + 1][indicator.position.x], Player):
            pass
        else:
            indicator.down()
            state.update_flag = True
            if state.player_moving_flag:
                level.units[indicator.prev_position.y][indicator.prev_position.x].down()
                update_unit_location()


def right_key_handler():
    if not indicator.position.x + 1 > (UNITS_LEN - 1):
        if state.player_moving_flag and isinstance(level.units[indicator.position.y][indicator.position.x + 1], Enemy):
            attack(level.units[indicator.position.y][indicator.position.x], level.units[indicator.position.y][indicator.position.x + 1])
            state.update_flag = True
        elif state.player_moving_flag and isinstance(level.units[indicator.position.y][indicator.position.x + 1], Player):
            pass
        else:
            indicator.right()
            state.update_flag = True
            if state.player_moving_flag:
                level.units[indicator.prev_position.y][indicator.prev_position.x].right()
                update_unit_location()


def left_key_handler():
    if not indicator.position.x - 1 < 0:
        if state.player_moving_flag and isinstance(level.units[indicator.position.y][indicator.position.x - 1], Enemy):
            attack(level.units[indicator.position.y][indicator.position.x], level.units[indicator.position.y][indicator.position.x - 1])
            state.update_flag = True
        elif state.player_moving_flag and isinstance(level.units[indicator.position.y][indicator.position.x - 1], Player):
            pass
        else:
            indicator.left()
            state.update_flag = True
            if state.player_moving_flag:
                level.units[indicator.prev_position.y][indicator.prev_position.x].left()
                update_unit_location()


def enter_key_handler():
    if state.player_moving_flag:
        state.player_moving_flag = False
    else:
        if isinstance(level.units[indicator.position.y][indicator.position.x], Player):
            state.player_moving_flag = True


# TODO: handle setting update_flage = True better
def event_handler(event_to_handle):
    if event_to_handle.type == pygame.QUIT:
        end_game('Game Over')
    elif event_to_handle.type == pygame.KEYUP:
        if event_to_handle.key == pygame.K_UP:
            up_key_handler()
        elif event_to_handle.key == pygame.K_DOWN:
            down_key_handler()
        elif event_to_handle.key == pygame.K_RIGHT:
            right_key_handler()
        elif event_to_handle.key == pygame.K_LEFT:
            left_key_handler()
        elif event_to_handle.key == pygame.K_RETURN:
            enter_key_handler()


def check_for_win():
    if not level.enemys:
        state.player_won = True


def end_game(msg):
    print(msg)
    sys.exit()


init_screen(level.terrain)
init_info_pane()
display_terrain_info()

render_unit(indicator)

for _player in level.players:
    render_unit(_player)

for _enemy in level.enemys:
    render_unit(_enemy)

pygame.display.update()

while 1:
    if state.player_won:
        end_game('You Win')

    state.update_flag = False

    for event in pygame.event.get():
        event_handler(event)

    if state.update_flag:
        check_for_win()
        clear_info_pane()
        move_indicator()
        update_unit_info()
        display_terrain_info()
        pygame.display.update()
