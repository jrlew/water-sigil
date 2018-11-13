"""
Placeholder
"""

from ..utils import image

class Job():
    def __init__(self, info):
        self.stats = info["stats"]
        self.image_active = image.load_png(info["image_active_path"])
        self.image_inactive = image.load_png(info["image_inactive_path"])
        self.image = self.image_active
        self.idle_1 = image.load_png(info["idle_1_path"])
        self.idle_2 = image.load_png(info["idle_2_path"])
        