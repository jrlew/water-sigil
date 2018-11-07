"""
Placeholder
"""

from .level import Level
from ..terrain import Terrain
from ..player import Player
from ..enemy import Enemy



class Intro(Level):
    def __init__(self):
        # TODO:This is gross and things need to be reorganized
        PLAIN = Terrain("Plain", "../data/images/green.png", 0, 0)
        MOUNT = Terrain("Mountain", "../data/images/brown.png", 2, 20)

        playerPositions = [(2, 2), (3, 2)] 
        enemyPositions = [(1, 4), (4, 4)]

        players = []
        for position in playerPositions:
            players.append(Player(position))
        enemys = []
        for position in enemyPositions:
            enemys.append(Enemy(position))

        Level.__init__(
            self,
            "Intro",
            players,
            enemys,
            [
                [MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, MOUNT, MOUNT, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
                [MOUNT, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNT],
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
