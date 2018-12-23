"""
Placeholder
"""

from .terrain import Terrain


class MountGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountGrass", "../../assets/terrain/mountain-bggrass.png", 2, 20)

