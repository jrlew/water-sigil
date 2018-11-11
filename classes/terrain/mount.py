"""
Placeholder
"""

from .terrain import Terrain


class Mount(Terrain):
    def __init__(self):
        Terrain.__init__(self, "Mount", "../../assets/terrain/mountain.png", 2, 20)

