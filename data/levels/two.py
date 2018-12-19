import pygame as pg

# TODO: Wrap classes better to avoid so many imports
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

from ..units.units import Units

from ..enemy import Enemy
from ..player import Player

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

level_params = {
    "terrain": [
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
    "players": pg.sprite.Group([
        Player((2, 2), Units.knight("blue")),
        Player((3, 3), Units.archer("blue"))
    ]),
    "enemys": pg.sprite.Group([
        Enemy((3, 6), Units.soldier("red")),
        Enemy((2, 7), Units.knight("red")),
    ]),
}