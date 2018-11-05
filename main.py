"""
Placeholder
"""

import sys
import pygame

from classes import enemy
from classes import player
from classes import indicator
from classes import state
from classes import terrain

BLACK = 0, 0, 0
size = width, height = 500, 500
PIXEL_SIZE = 16
FONT_SIZE = 16

# TODO: change these to be info_pane_width and info_pane_height
msg_width = 80 
msg_height = 160

UP_KEY = 273
DOWN_KEY = 274
RIGHT_KEY = 275
LEFT_KEY = 276
ENTER_KEY = 13

playerPositions = [(2, 2), (3, 2)] 
enemyPositions = [(1, 4), (4, 4)]
indicatorPos = (0, 0)

STATE = state.State()

# Anything Pygame related has to be used after the init() line
pygame.init()
screen = pygame.display.set_mode(size)

players = []
for position in playerPositions:
    players.append(player.Player(position, True))
# _player = player.Player(playerPos, True)

indicator = indicator.Indicator(indicatorPos, True)

enemys = []
for position in enemyPositions:
    enemys.append(enemy.Enemy(position, False))

# ter_plain = pygame.image.load("data/green.png").convert()
# ter_mount = pygame.image.load("data/brown.png").convert()

ter_plain = terrain.Terrain("Plain", "../data/green.png", 0 , 0)
ter_mount = terrain.Terrain("Mountain", "../data/brown.png", 2, 20) 

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
            screen.blit(col.image, (x_coord, y_coord))
            x_coord += PIXEL_SIZE
        y_coord += PIXEL_SIZE
        pygame.display.update()


def render_unit(unit):
    screen.blit(unit.image, (unit.position.x * PIXEL_SIZE, unit.position.y * PIXEL_SIZE))


def move_indicator():    
    screen.blit(MAP_TERRAIN[indicator.prev_position.y][indicator.prev_position.x].image, 
(indicator.prev_position.x * PIXEL_SIZE, indicator.prev_position.y * PIXEL_SIZE)) # TODO move terrain into a class so it can use render_unit()
    if not UNITS[indicator.prev_position.y][indicator.prev_position.x] == 0:
        render_unit(UNITS[indicator.prev_position.y][indicator.prev_position.x])
        # screen.blit(UNITS[indicator.prev_position.x][indicator.prev_position.x].image, (indicator.prev_position.x * PIXEL_SIZE, indicator.prev_position.y * PIXEL_SIZE))

    screen.blit(MAP_TERRAIN[indicator.position.y][indicator.position.x].image, (indicator.position.x * PIXEL_SIZE, 
indicator.position.y * PIXEL_SIZE)) # TODO move terrain into a class so it can use render_unit()
    if not UNITS[indicator.position.y][indicator.position.x] == 0:
        render_unit(UNITS[indicator.position.y][indicator.position.x])
        # screen.blit(UNITS[indicator.position.y][indicator.position.x].image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))

    render_unit(indicator)
    # screen.blit(indicator.image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))
    pygame.display.update()


def update_unit_location():
    UNITS[indicator.position.y][indicator.position.x] = UNITS[indicator.prev_position.y][indicator.prev_position.x]
    UNITS[indicator.prev_position.y][indicator.prev_position.x] = 0

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


def clear_info_pane():
    x_offset = len(MAP_TERRAIN[0]) * PIXEL_SIZE
    pygame.draw.rect(screen, BLACK, [x_offset, 0, msg_width, msg_height], 0)


def display_terrain_info():
    terrain = MAP_TERRAIN[indicator.position.y][indicator.position.x]
    terrain_info = [
        "{type}".format(type = terrain.type),
        "Def: {def_adjustment}".format(def_adjustment = terrain.def_adjustment),
        "Evd: {evasion_adjustment}".format(evasion_adjustment = terrain.evasion_adjustment),
    ]
    x_offset = len(UNITS[0]) * PIXEL_SIZE
    y_offset = 80
    for line in terrain_info:
        screen.blit(FONT.render(line, 1, (200, 200, 200)), (x_offset, y_offset))
        y_offset += (FONT_SIZE + 4)
    pygame.display.update()


def update_unit_info():
    if not UNITS[indicator.position.y][indicator.position.x] == 0:
        display_unit_info(UNITS[indicator.position.y][indicator.position.x].stats)


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
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].up()
                    update_unit_location()
        elif event_to_handle.key == DOWN_KEY:
            if not indicator.position.y + 1 > 4:
                indicator.down()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].down()
                    update_unit_location()
        elif event_to_handle.key == RIGHT_KEY:
            if not indicator.position.x + 1 > 4:
                indicator.right()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].right()
                    update_unit_location()
        elif event_to_handle.key == LEFT_KEY:
            if not indicator.position.x - 1 < 0:
                indicator.left()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].left()
                    update_unit_location()
        elif event_to_handle.key == ENTER_KEY:
            print(STATE.player_moving_flag)
            if STATE.player_moving_flag:
                STATE.player_moving_flag = False
            else:
                if type(UNITS[indicator.position.y][indicator.position.x]) == player.Player:
                    STATE.player_moving_flag = True

# TODO change this to check for enemies to be 0
# def check_for_win():
#     if _player.position.x == enemys[0].position.x and _player.position.y == enemys[0].position.y:
#         STATE.player_won = True


def end_game(msg):
    print(msg)
    sys.exit()


init_screen(MAP_TERRAIN)

render_unit(indicator)
# screen.blit(indicator.image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE))

for _player in players:
    UNITS[_player.position.y][_player.position.x] = _player
    render_unit(_player)
    # screen.blit(_player.image, (_player.position.y * PIXEL_SIZE, _player.position.x * PIXEL_SIZE))

for enemy in enemys:
    UNITS[enemy.position.y][enemy.position.x] = enemy
    render_unit(enemy)
    # screen.blit(enemy.image, (enemy.position.y * PIXEL_SIZE, enemy.position.x * PIXEL_SIZE))

# for rows in UNITS:
#     for column in rows:
#         if not column == 0:
#             screen.blit(column.image, (column.position.x * PIXEL_SIZE, column.position.y * PIXEL_SIZE))


pygame.display.update()

for rows in MAP_TERRAIN:
    print(rows)

for rows in UNITS:
    print(rows)

while 1:
    if STATE.player_won:
        end_game('You Win')

    STATE.update_flag = False

    for event in pygame.event.get():
        event_handler(event)

    if STATE.update_flag:
        # check_for_win()
        clear_info_pane()
        move_indicator()
        update_unit_info()
        display_terrain_info()
