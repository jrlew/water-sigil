"""
Placeholder
"""

from .terrain import Terrain

WHITE = 255, 255, 255


class Fortress(Terrain):
    def __init__(self):
        Terrain.__init__(self, "Fortress", "../../data/images/fortress.png", 2, 40)
        self.image.set_colorkey(WHITE)