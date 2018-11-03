"""
Placeholder
"""

import sys
import pygame

from classes import enemy
from classes import player
from classes import indicator
from classes import state

BLACK = 0, 0, 0
size = width, height = 500, 500
PIXEL_SIZE = 16
FONT_SIZE = 16

msg_width = 80 
msg_height = 80

UP_KEY = 273
DOWN_KEY = 274
RIGHT_KEY = 275
LEFT_KEY = 276
ENTER_KEY = 13

playerPos = (2, 2)
enemyPositions = [(1, 4), (4, 4)]
indicatorPos = (0, 0)

STATE = state.State()

# Anything Pygame related has to be used after the init() line
pygame.init()
screen = pygame.display.set_mode(size)

_player = player.Player(playerPos, True)
indicator = indicator.Indicator(indicatorPos, True)

enemys = []
for position in enemyPositions:
    enemys.append(enemy.Enemy(position, False))

ter_plain = pygame.image.load("data/green.png").convert()
ter_mount = pygame.image.load("data/brown.png").convert()

FONT = pygame.font.Font(None, FONT_SIZE)

MAP_TERRAIN = [
    [ter_mount, ter_mount, ter_mount, ter_mount, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain]
]

UNITS = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def init_screen(map_array):
    y_coord = 0
    for row in map_array:
        x_coord = 0
        for col in row:
            screen.blit(col, (y_coord, x_coord))
            x_coord += PIXEL_SIZE
        y_coord += PIXEL_SIZE
        pygame.display.update()


def move_indicator():
    screen.blit(MAP_TERRAIN[indicator.prev_position.x][indicator.prev_position.y], (indicator.prev_position.x * PIXEL_SIZE, indicator.prev_position.y * PIXEL_SIZE))
    if not UNITS[indicator.prev_position.x][indicator.prev_position.y] == 0:
        screen.blit(UNITS[indicator.prev_position.x][indicator.prev_position.y].image, (indicator.prev_position.x * PIXEL_SIZE, indicator.prev_position.y * PIXEL_SIZE))

    screen.blit(MAP_TERRAIN[indicator.position.x][indicator.position.y], (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))
    if not UNITS[indicator.position.x][indicator.position.y] == 0:
        screen.blit(UNITS[indicator.position.x][indicator.position.y].image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))

    screen.blit(indicator.image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))
    pygame.display.update()


def update_unit_location():
    UNITS[indicator.position.x][indicator.position.y] = UNITS[indicator.prev_position.x][indicator.prev_position.y]
    UNITS[indicator.prev_position.x][indicator.prev_position.y] = 0

def display_unit_info(stats):
    info = [
        'HP: {hp} / {maxhp}'.format(hp=stats.current_hp,
                                    maxhp=stats.max_hp),
        'STR: {str}'.format(str=stats.strength),
        'DEF: {defense}'.format(defense=stats.defense)
    ]
    x_offset = len(UNITS[0]) * PIXEL_SIZE
    y_offset = 0
    for line in info:
        screen.blit(FONT.render(line, 1, (200, 200, 200)), (x_offset, y_offset))
        y_offset += (FONT_SIZE + 4)
    pygame.display.update()


def clear_unit_info():
    x_offset = len(MAP_TERRAIN[0]) * PIXEL_SIZE
    pygame.draw.rect(screen, BLACK, [x_offset, 0, msg_width, msg_height], 0)


def update_unit_info():
    if UNITS[indicator.position.x][indicator.position.y] == 0:
        clear_unit_info()
    else:
        display_unit_info(UNITS[indicator.position.x][indicator.position.y].stats)


def event_handler(event_to_handle):
    if event_to_handle.type == pygame.QUIT:
        end_game('Game Over')

    elif event_to_handle.type == pygame.KEYUP:
        # print(event_to_handle.key)
        if event_to_handle.key == UP_KEY:
            if not indicator.position.y - 1 < 0:
                indicator.up()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    _player.up()
                    update_unit_location()
        elif event_to_handle.key == DOWN_KEY:
            if not indicator.position.y + 1 > 4:
                indicator.down()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    _player.down()
                    update_unit_location()
        elif event_to_handle.key == RIGHT_KEY:
            if not indicator.position.x + 1 > 4:
                indicator.right()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    _player.right()
                    update_unit_location()
        elif event_to_handle.key == LEFT_KEY:
            if not indicator.position.x - 1 < 0:
                indicator.left()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    _player.left()
                    update_unit_location()
        elif event_to_handle.key == ENTER_KEY:
            print(STATE.player_moving_flag)
            if STATE.player_moving_flag:
                STATE.player_moving_flag = False
            else:
                if type(UNITS[indicator.position.x][indicator.position.y]) == player.Player:
                    STATE.player_moving_flag = True


def check_for_win():
    if _player.position.x == enemys[0].position.x and _player.position.y == enemys[0].position.y:
        STATE.player_won = True


def end_game(msg):
    print(msg)
    sys.exit()


init_screen(MAP_TERRAIN)

screen.blit(indicator.image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))
UNITS[_player.position.x][_player.position.y] = _player
for enemy in enemys:
    UNITS[enemy.position.x][enemy.position.y] = enemy

for rows in UNITS:
    for column in rows:
        if not column == 0:
            screen.blit(
                column.image, (column.position.x * PIXEL_SIZE, column.position.y * PIXEL_SIZE))


pygame.display.update()

while 1:
    if STATE.player_won:
        end_game('You Win')

    STATE.update_flag = False

    for event in pygame.event.get():
        event_handler(event)

    if STATE.update_flag:
        check_for_win()
        move_indicator()
        update_unit_info()
