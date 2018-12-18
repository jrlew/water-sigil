"""
Placeholder
"""

from .terrain import Terrain


# TODO: Separate this from Terrain and move to a difference folder
class AttackOverlay(Terrain):
    def __init__(self):
        Terrain.__init__(self, "AttackOverlay", "../../assets/common/red-outline.png", 1, 10)
        self.image.set_colorkey((255, 255, 255))