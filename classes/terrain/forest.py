"""
Placeholder
"""

from .terrain import Terrain


class Forest(Terrain):
    def __init__(self):
        Terrain.__init__(self, "Forest", "../../assets/terrain/forest.png", 1, 10)