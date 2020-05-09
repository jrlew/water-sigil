"""
Placeholder
"""

import os
import pygame

# TODO: fix errors to be useful
def load_png(name, override_alpha=False):
    """ Load image and return image object"""
    fullname = os.path.join(os.path.dirname(__file__), "../../assets", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None or override_alpha:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print('Cannot load image:', fullname)
        raise pygame.error
    return image