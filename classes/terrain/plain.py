"""
Placeholder
"""

from .terrain import Terrain

class Plain(Terrain):
    def __init__(self):
        self = Terrain.__init__(self, "Plain", "../../data/images/green.png", 0, 0)

