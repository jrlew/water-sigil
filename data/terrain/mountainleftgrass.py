"""
Placeholder
"""

from .terrain import Terrain


class MountLeftGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountLeftGrass", "../../assets/terrain/mountain-left-bggrass.png", 2, 20)

