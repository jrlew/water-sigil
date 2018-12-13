"""
Placeholder
"""

from .terrain import Terrain


# TODO: Separate this from Terrain and move to a difference folder
class MoveOverlay(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MoveOverlay", "../../assets/common/blue-outline.png", 0, 0)
        self.image.set_colorkey((255, 255, 255))