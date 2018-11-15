import pygame as pg
from .state import State

from .terrain.plain import Plain
from .terrain.mountain import Mount
from .terrain.mountainbottom import MountBottom
from .terrain.mountainbottomleftgrass import MountBottomLeftGrass
from .terrain.mountainbottomrightgrass import MountBottomRightGrass
from .terrain.mountaingrass import MountGrass
from .terrain.mountainleftgrass import MountLeftGrass
from .terrain.mountainleftmountain import MountLeftMount
from .terrain.mountainrightgrass import MountRightGrass
from .terrain.mountainrightmountain import MountRightMount
from .terrain.mountaintopleftgrass import MountTopLeftGrass
from .terrain.forest import Forest
from .terrain.fortress import Fortress

from .indicator import Indicator


class LevelInit(State):
    """
    Parent class for individual game states to inherit from. 
    """

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
        self.persist = {}
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
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 

        dt: time since last frame
        """
        self.persist["terrain"] = self.terrain
        self.persist["PIXEL_SIZE"] = 32
        self.persist["indicator"] = self.indicator

    def draw(self, screen):
        """
        Draw everything to the screen.
        """
        screen.init_screen(self.persist["terrain"])
        # PIXEL_SIZE = 32
        # y_coord = 0
        # for row in self.terrain:
        #     x_coord = 0
        #     for col in row:
        #         screen.display.blit(col.image, (x_coord, y_coord))
        #         x_coord += self.PIXEL_SIZE
        #     y_coord += self.PIXEL_SIZE
        # screen.display.blit(self.persist["indicator"].image, (self.persist["indicator"].position.x * self.PIXEL_SIZE, self.persist["indicator"].position.y * self.PIXEL_SIZE))
        screen.render_unit(self.persist["indicator"])
        self.done = True
