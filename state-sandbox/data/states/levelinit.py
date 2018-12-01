import pygame as pg
from .state import State

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

from ..indicator import Indicator

from ..enemy import Enemy
from ..player import Player

from ..units.knight import Knight
from ..units.soldier import Soldier

from ..persist import Persist

class LevelInit(State):
    def __init__(self):
        super(LevelInit, self).__init__()
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
        
        self.done = False
        self.quit = False
        self.next_state = "Player_Phase"
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = Persist()
        self.font = pg.font.Font(None, 24)
        self.PIXEL_SIZE = 32
        self.terrain = [
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
        ]
        self.indicator = Indicator((0, 0))


    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        self.persist.terrain = self.terrain
        self.persist.PIXEL_SIZE = 32
        self.persist.indicator = self.indicator
        self.persist.enemys = pg.sprite.Group([
            Enemy((3, 6), Soldier("red")),
            Enemy((2, 7), Knight("red")),
        ])
        self.persist.players = pg.sprite.Group([
            Player((2, 2), Knight("blue"))
        ])
        self.persist.all_units = pg.sprite.Group(self.persist.players.sprites() + self.persist.enemys.sprites())
        self.persist.units = [
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
        ]
        for unit in self.persist.all_units.sprites():
            self.persist.units[unit.position.y][unit.position.x] = unit

    def draw(self, screen):
        screen.init_info_pane()
        screen.init_context_menu()
        screen.init_screen(self.persist.terrain)
        screen.render_unit(self.persist.indicator)
        screen.display_terrain_info(self.persist.terrain[self.persist.indicator.prev_position.y][self.persist.indicator.prev_position.x])
        for unit in self.persist.all_units.sprites():
            screen.render_unit(unit)
        self.done = True
