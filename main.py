import sys

import pygame as pg

from data.game import Game
from data.screen import Screen

pg.init()
screen = Screen()

# This import must be after pginit() and screen = Screen() due to state files relying on loading images
# due to level_params being a dictionary that instantiates objects depending on pygames image loading
# TODO: Refactor level_params to not do that ^
from data.states.states import states

game = Game(screen, states, "Level_Select")
game.run()
pg.quit()
sys.exit()
