"""
Placeholder
"""

from .level import Level

from ..terrain.plain import Plain
from ..terrain.mount import Mount
from ..terrain.forest import Forest
from ..terrain.fortress import Fortress

from ..player import Player
from ..enemy import Enemy

from ..units.soldier import Soldier
from ..units.knight import Knight


class Intro(Level):
    def __init__(self):
        PLAIN = Plain()
        MOUNT = Mount()
        FREST = Forest()
        FTRSS = Fortress()

        players = [
            # Player((1, 4), Soldier("blue")),
            Player((3, 4), Knight("blue")),
            # Player((3, 3), Soldier("blue")),
        ]

        enemys = [
            Enemy((3, 6), Soldier("red")),
            Enemy((2, 7), Knight("red")),
            # Enemy((7, 2), Soldier("red")),
            # Enemy((8, 3), Soldier("red")),
            # Enemy((6, 5), Soldier("red")),
        ]

        Level.__init__(
            self,
            "Intro",
            players,
            enemys,
            [
                [MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, FREST, FREST, FREST, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, FREST, FREST, FREST, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, FTRSS, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT],
                [MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT],
            ],
            [
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
            ],
        )
