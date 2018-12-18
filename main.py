import sys
import pygame as pg

from data.game import Game
from data.screen import Screen

# TODO: Remove these
from data.levelone import Level1
from data.leveltwo import Level2

pg.init()
screen = Screen()

# TODO: Point these to the real levels one and two
levels = {
    "Level1": Level1,
    "Level2": Level2,
}

screen.display_context_message("> Level One     Level Two")
pg.display.update()

indicator_state = True
waiting = True
while waiting:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.quit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                indicator_state = not indicator_state
                if indicator_state:
                    screen.display_context_message(">Level One    Level Two")
                else:
                    screen.display_context_message(" Level One   >Level Two")
                pg.display.update()
            if event.key == pg.K_RETURN:
                waiting = False

if indicator_state:
    print('Selecting Level One')
else:
    print('Selecting Level Two')


from data.states.states import states

#TODO: replace levelone.py with game.py that accepts a level file as paramter
game = levels["Level1"](screen, states, "Level_Init")
game.run()
pg.quit()
sys.exit()
