"""
Placeholder
"""

from .terrain import Terrain


class MountRightGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountRightGrass", "../../assets/terrain/mountain-right-bggrass.png", 2, 20)

