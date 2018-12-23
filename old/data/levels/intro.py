"""
Placeholder
"""

from .level import Level

from ..terrain.plain import Plain
from ..terrain.mountain import Mount
from ..terrain.mountainbottom import MountBottom
from ..terrain.mountainbottomleftgrass import MountBottomLeftGrass
from ..terrain.mountainbottomrightgrass import MountBottomRightGrass
from ..terrain.mountaingrass import MountGrass
from ..terrain.mountainleftgrass import MountLeftGrass
from ..terrain.mountainleftmountain import MountLeftMount
from ..terrain.mountainrightgrass import MountRightGrass
from ..terrain.mountainrightmountain import MountRightMount
from ..terrain.mountaintopleftgrass import MountTopLeftGrass
from ..terrain.forest import Forest
from ..terrain.fortress import Fortress

from ..player import Player
from ..enemy import Enemy

from ..units.soldier import Soldier
from ..units.knight import Knight
from ..units.warden import Warden


class Intro(Level):
    def __init__(self):
        PLAIN = Plain()
        MOUNT = Mount()
        MOUNTBOT = MountBottom()
        MOUNTBOTLEFTGRASS = MountBottomLeftGrass()
        MOUNTBOTRIGHTGRASS = MountBottomRightGrass()
        MOUNTGRASS = MountGrass()
        MOUNTLEFTGRASS = MountLeftGrass()
        MOUNTLEFTMOUNT = MountLeftMount()
        MOUNTRIGHTGRASS = MountRightGrass()
        MOUNTRIGHTMOUNT = MountRightMount()
        MOUNTTOPLEFTGRASS = MountTopLeftGrass()
        FREST = Forest()
        FTRSS = Fortress()

        players = [
            # Player((1, 4), Soldier("blue")),
            Player((3, 4), Warden("blue")),
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
                [MOUNT, MOUNTBOT, MOUNTBOT, MOUNTBOT, MOUNT, MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS, MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTBOTLEFTGRASS, MOUNTBOTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, FREST, FREST, FREST, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, FREST, FREST, FREST, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, FTRSS, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, PLAIN, MOUNTLEFTGRASS],
                [MOUNTRIGHTGRASS, PLAIN, PLAIN, PLAIN, MOUNTTOPLEFTGRASS, MOUNTGRASS, MOUNTGRASS, MOUNTGRASS, MOUNTGRASS, MOUNT],
                [MOUNT, MOUNTGRASS, MOUNTGRASS, MOUNTGRASS, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT, MOUNT],
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
