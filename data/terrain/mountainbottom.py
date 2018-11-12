"""
Placeholder
"""

from .terrain import Terrain


class MountBottom(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountBottom", "../../assets/terrain/mountain-bottom.png", 2, 20)

