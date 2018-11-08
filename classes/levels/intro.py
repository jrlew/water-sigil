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


class Intro(Level):
    def __init__(self):
        # TODO: this is kinda gross. Tiles Classes that has the possiblities pre-instantiated?
        PLAIN = Plain()
        MOUNT = Mount()
        FREST = Forest()
        FTRSS = Fortress()

        # TODO: This is going to get complicated and messy once it expands varied types on units...
        playerPositions = [(2, 2), (3, 2)]
        playerStats = {
            "name": "Player",
            "hp": 20,
            "strength": 8,
            "defense": 4,
            "accuracy": 120,
            "evasion": 25,
        }
        enemyPositions = [(1, 4), (4, 4)]
        enemyStats = {
            "name": "Enemy",
            "hp": 14,
            "strength": 4,
            "defense": 2,
            "accuracy": 90,
            "evasion": 30,
        }

        players = []
        for position in playerPositions:
            players.append(Player(position, playerStats))
        enemys = []
        for position in enemyPositions:
            enemys.append(Enemy(position, enemyStats))

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
