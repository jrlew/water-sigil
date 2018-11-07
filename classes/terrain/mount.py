"""
Placeholder
"""

from .terrain import Terrain


class Mount(Terrain):
    def __init__(self):
        Terrain.__init__(self, "Mount", "../../data/images/brown.png", 2, 20)

