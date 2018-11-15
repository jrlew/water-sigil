"""
Placeholder
"""

from .terrain import Terrain


class MountTopLeftGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountTopLeftGrass", "../../assets/terrain/mountain-top-left-bggrass.png", 2, 20)

