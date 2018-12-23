"""
Placeholder
"""

from .terrain import Terrain


class MountBottomRightGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountBottomRightGrass", "../../assets/terrain/mountain-bottom-right-bggrass.png", 2, 20)

