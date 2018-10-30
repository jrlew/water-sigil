import sys
import pygame
import os

from classes import enemy
from classes import player
from classes import indicator

black = 0, 0, 0
white = 255, 255, 255
size = width, height = 500, 500
pixelSize = 16
fontSize = 16

upKey = 273
downKey = 274
rightKey = 275
leftKey = 276
enterKey = 13

pygame.init()
screen = pygame.display.set_mode(size)

playerPos = { "x": 2, "y": 2 }
enemyPositions = [ { "x": 1, "y": 4 }, { "x": 4, "y": 4 } ]
indicatorPos = { "x": 0, "y": 0 }

enemys = []
for position in enemyPositions:
    enemys.append(enemy.Enemy(position))

player = player.Player(playerPos)
indicator = indicator.Indicator(indicatorPos)

ter_plain = pygame.image.load("data/green.png").convert()
ter_mount = pygame.image.load("data/brown.png").convert()

font = pygame.font.Font(None, fontSize)

background = [
    [ter_mount, ter_mount, ter_mount, ter_mount, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_mount],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain],
    [ter_mount, ter_plain, ter_plain, ter_plain, ter_plain]
]

units = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def initScreen(screen, screenArray):
    y_coord = 0
    for y in screenArray:
        x_coord = 0
        for x in y:
            screen.blit(x, (y_coord, x_coord))
            x_coord += pixelSize
        y_coord += pixelSize
        pygame.display.update()


def moveIcon(oldIconPos, newIconPos, icon):
    screen.blit(background[oldIconPos["x"]][oldIconPos["y"]], (oldIconPos["x"]*pixelSize, oldIconPos["y"]*pixelSize))
    screen.blit(icon, (newIconPos["x"]*pixelSize, newIconPos["y"]*pixelSize))
    if (oldIconPos == player.position):
        screen.blit(player.image, (player.position["x"]*pixelSize, player.position["y"]*pixelSize))
    if (oldIconPos == enemys[0].position):
        screen.blit(enemys[0].image, (enemys[0].position["x"]*pixelSize, enemys[0].position["y"]*pixelSize))
    pygame.display.update()


def displayUnitInfo(hp, maxhp, strength, defense):
    if hp:
        info = [
            'HP: {hp} / {maxhp}'.format(hp = hp, maxhp = maxhp),
            'STR: {str}'.format(str = strength),
            'DEF: {defense}'.format(defense = defense)
        ]
        x = 80 # magic number please fix
        y = 0
        for line in info:
            screen.blit(font.render(line, 1, (200, 200, 200)), (x, y))
            y += (fontSize + 4)
    pygame.display.update()
    

def clearUnitInfo():
    pygame.draw.rect(screen, black, [80, 0, 80, 80], 0) # fix these magic numbers
    pygame.display.flip()

initScreen(screen, background)

screen.blit(indicator.image, (indicator.position["x"]*pixelSize, indicator.position["y"]*pixelSize))
units[player.position["x"]][player.position["y"]] = player
for enemy in enemys:
    units[enemy.position["x"]][enemy.position["y"]] = enemy

for rows in units:
    for square in rows:
        if not square == 0:
            screen.blit(square.image, (square.position["x"]*pixelSize, square.position["y"]*pixelSize))


pygame.display.update()

playerMovingFlag = False

while 1:
    updateFlag = False
    oldPlayerPos = dict(player.position)
    oldIndicatorPos = dict(indicator.position)

    # TODO: Separate into event handler functions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            # print(event.key)
            if event.key == upKey:
                if not indicator.position["y"] + -1 < 0:
                    indicator.up()
                    updateFlag = True
                    if (playerMovingFlag):
                        player.up()
            elif event.key == downKey:
                if not indicator.position["y"] + 1 > 4:
                    indicator.down()
                    updateFlag = True
                    if (playerMovingFlag):
                        player.down()
            elif event.key == rightKey:
                if not indicator.position["x"] + 1 > 4:
                    indicator.right()
                    updateFlag = True
                    if (playerMovingFlag):
                        player.right()
            elif event.key == leftKey:
                if not indicator.position["x"] + -1 < 0:
                    indicator.left()
                    updateFlag = True
                    if (playerMovingFlag):
                        player.left()
            elif event.key == enterKey:
                if (playerMovingFlag):
                    playerMovingFlag = False
                else:
                    if indicator.position == player.position:
                        playerMovingFlag = True

    if updateFlag:
        if player.position == enemys[0].position:
            print('You win')
            sys.exit()
        else:
            if (playerMovingFlag):
                moveIcon(oldPlayerPos, player.position, player.image)
            moveIcon(oldIndicatorPos, indicator.position, indicator.image)

        # TODO Separate out into functions
        if units[indicator.position["x"]][indicator.position["y"]] == 0:
            clearUnitInfo()
        else:
            displayUnitInfo(**units[indicator.position["x"]][indicator.position["y"]].getStats())
