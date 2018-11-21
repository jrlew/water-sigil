"""
Placeholder
"""

from .terrain import Terrain

class Plain(Terrain):
    def __init__(self):
        self = Terrain.__init__(self, "Plain", "../../assets/terrain/cobblestone.png", 0, 0)

