"""
Placeholder
"""

from .terrain import Terrain


class Forest(Terrain):
    def __init__(self):
        Terrain.__init__(self, "Forest", "../../data/images/dark_green.png", 1, 10)