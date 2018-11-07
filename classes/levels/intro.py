"""
Placeholder
"""

from .level import Level
from ..terrain.plain import Plain
from ..terrain.mount import Mount
from ..player import Player
from ..enemy import Enemy



class Intro(Level):
    def __init__(self):
        # TODO: this is kinda gross. Tiles Classes that has the possiblities pre-instantiated?
        PLAIN = Plain()
        MOUNT = Mount()

        # TODO: This is going to get complicated and messy once it expands varied types on units...
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
