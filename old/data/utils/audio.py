"""
Placeholder
"""

import os
import pygame

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(os.path.dirname(__file__), "../../assets", name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound: ', fullname)
        raise SystemExit
    return sound