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
WHITE = 255, 255, 255
size = width, height = 480, 360
PIXEL_SIZE = 32
FONT_SIZE = 24

# TODO: change these to be info_pane_width and info_pane_height
MSG_WIDTH = 150
MSG_HEIGHT = 120

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

indicator = indicator.Indicator(indicatorPos, True)

enemys = []
for position in enemyPositions:
    enemys.append(enemy.Enemy(position, False))

ter_plain = terrain.Terrain("Plain", "../data/green.png", 0 , 0)
ter_mount = terrain.Terrain("Mountain", "../data/brown.png", 2, 20) 

FONT = pygame.font.Font(None, FONT_SIZE)

MAP_TERRAIN = [
    [ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount, ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount, ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount],
    [ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount, ter_mount],
]

UNITS = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

UNITS_LEN = 10 # TODO: temp value until MAP_TERRAIN gets moved to a separate file and UNITS gets generated based on MAP_TERRAIN values
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


def move_indicator():    
    screen.blit(MAP_TERRAIN[indicator.prev_position.y][indicator.prev_position.x].image, (indicator.prev_position.x * PIXEL_SIZE, indicator.prev_position.y * PIXEL_SIZE)) # TODO move terrain into a class so it can use render_unit()
    if not UNITS[indicator.prev_position.y][indicator.prev_position.x] == 0:
        render_unit(UNITS[indicator.prev_position.y][indicator.prev_position.x])

    screen.blit(MAP_TERRAIN[indicator.position.y][indicator.position.x].image, (indicator.position.x * PIXEL_SIZE, indicator.position.y * PIXEL_SIZE)) # TODO move terrain into a class so it can use render_unit()
    if not UNITS[indicator.position.y][indicator.position.x] == 0:
        render_unit(UNITS[indicator.position.y][indicator.position.x])

    render_unit(indicator)


def update_unit_location():
    UNITS[indicator.position.y][indicator.position.x] = UNITS[indicator.prev_position.y][indicator.prev_position.x]
    UNITS[indicator.prev_position.y][indicator.prev_position.x] = 0


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
        'HP: {hp} / {maxhp}'.format(hp=stats.current_hp,
                                    maxhp=stats.max_hp),
        'STR: {str}'.format(str=stats.strength),
        'DEF: {defense}'.format(defense=stats.defense)
    ]
    y_offset = 34
    for line in info:
        screen.blit(FONT.render(line, 1, (200, 200, 200)), (INFO_PANE_X_OFFSET + 8, y_offset))
        y_offset += (FONT_SIZE + 4)


def clear_info_pane():
    pygame.draw.rect(screen, BLACK, [INFO_PANE_X_OFFSET + 4, 34, MSG_WIDTH, MSG_HEIGHT], 0)
    pygame.draw.rect(screen, BLACK, [INFO_PANE_X_OFFSET + 4, 195, MSG_WIDTH, MSG_HEIGHT], 0)


def display_terrain_info():
    ter = MAP_TERRAIN[indicator.position.y][indicator.position.x]
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
    if not UNITS[indicator.position.y][indicator.position.x] == 0:
        display_unit_info(UNITS[indicator.position.y][indicator.position.x].stats)


def display_context_message(msg_text):
    pygame.draw.rect(screen, BLACK, [8, 329, 440, 26], 0)
    screen.blit(FONT.render(msg_text, 1, (200, 200, 200)), (8, 329))


# TODO: This is pretty gross
def checkForEnemyDeath(unit, y_index, x_index):
    if unit.stats.current_hp < 1:
        UNITS[y_index][x_index] = 0
        enemys.pop() # TODO: This is real dirty and should be done better
        screen.blit(MAP_TERRAIN[y_index][x_index].image, (x_index* PIXEL_SIZE, y_index * PIXEL_SIZE))


def event_handler(event_to_handle):
    if event_to_handle.type == pygame.QUIT:
        end_game('Game Over')

    # TODO: handle setting update_flage = True better
    elif event_to_handle.type == pygame.KEYUP:
        if event_to_handle.key == UP_KEY:
            # TODO Functionify this, figure out check for enemy instead of not 0, add attack checks to all movements options
            if STATE.player_moving_flag and not UNITS[indicator.position.y - 1][indicator.position.x] == 0:
                UNITS[indicator.position.y - 1][indicator.position.x].stats.current_hp -= UNITS[indicator.position.y][indicator.position.x].stats.strength
                display_context_message("Attacked Enemy. Remaining HP: {remaining_hp}".format(remaining_hp=UNITS[indicator.position.y - 1][indicator.position.x].stats.current_hp))
                checkForEnemyDeath(UNITS[indicator.position.y - 1][indicator.position.x], indicator.position.y - 1, indicator.position.x)
                STATE.update_flag = True
            elif not indicator.position.y - 1 < 0:
                indicator.up()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].up()
                    update_unit_location()
        elif event_to_handle.key == DOWN_KEY:
            if not indicator.position.y + 1 > (UNITS_LEN - 1):
                indicator.down()
                STATE.update_flag = True
                if STATE.player_moving_flag:
                    UNITS[indicator.prev_position.y][indicator.prev_position.x].down()
                    update_unit_location()
        elif event_to_handle.key == RIGHT_KEY:
            if not indicator.position.x + 1 > (UNITS_LEN - 1):
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
            if STATE.player_moving_flag:
                STATE.player_moving_flag = False
            else:
                if type(UNITS[indicator.position.y][indicator.position.x]) == player.Player:
                    STATE.player_moving_flag = True


def check_for_win():
    if len(enemys) == 0:
        STATE.player_won = True


def end_game(msg):
    print(msg)
    sys.exit()


init_screen(MAP_TERRAIN)
init_info_pane()
display_terrain_info()
display_context_message('Testing Testing Testing')
display_context_message('Second time')

render_unit(indicator)

for _player in players:
    UNITS[_player.position.y][_player.position.x] = _player
    render_unit(_player)

for enemy in enemys:
    UNITS[enemy.position.y][enemy.position.x] = enemy
    render_unit(enemy)

pygame.display.update()

while 1:
    if STATE.player_won:
        end_game('You Win')

    STATE.update_flag = False

    for event in pygame.event.get():
        event_handler(event)

    if STATE.update_flag:
        check_for_win()
        clear_info_pane()
        move_indicator()
        update_unit_info()
        display_terrain_info()
        pygame.display.update()
