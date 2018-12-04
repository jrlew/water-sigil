import sys
import pygame as pg
from data.game import Game
from data.levelone import Level1
from data.leveltwo import Level2

from data.states.levelinit import LevelInit
from data.states.playerphase import PlayerPhase
from data.states.unitphase import UnitPhase
from data.states.unitattack import UnitAttackPhase
from data.states.enemyphase import EnemyPhase

from data.screen import Screen

pg.init()
screen = Screen()

levels = {
    "Level1": Level1,
    "Level2": Level2,
}

chosen_level = ""
waiting = True

# TODO: Render some kind of Level Select
pg.display.update()

while waiting:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.quit()
        if event.type == pg.KEYUP:
            print('>>>>>>>>>>>>>>>> Keyup means level 1')
            chosen_level = "Level1"
            waiting = False
        elif event.type == pg.MOUSEBUTTONUP:
            print('>>>>>>>>>>>>>>>> Mouseup means level 2') # Always one for now for testing
            chosen_level = "Level1"
            waiting = False

states = {
    "Level_Init": LevelInit(),
    "Player_Phase": PlayerPhase(),
    "UnitPhase": UnitPhase(),
    "UnitAttackPhase": UnitAttackPhase(),
    "EnemyPhase": EnemyPhase(),
}

game = levels[chosen_level](screen, states, "Level_Init")
game.run()
pg.quit()
sys.exit()
