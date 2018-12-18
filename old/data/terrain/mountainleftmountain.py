"""
Placeholder
"""

from .terrain import Terrain


class MountLeftMount(Terrain):
    def __init__(self):
        Terrain.__init__(self, "MountLeftMount", "../../assets/terrain/mountain-left-bgmountain.png", 2, 20)

