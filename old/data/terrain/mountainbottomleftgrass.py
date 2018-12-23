"""
Placeholder
"""

from .terrain import Terrain


class MountBottomLeftGrass(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountBottomLeftGrass", "../../assets/terrain/mountain-bottom-left-bggrass.png", 2, 20)

