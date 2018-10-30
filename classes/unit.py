import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, initPos):
        self.position = {
            "x": initPos["x"],
            "y": initPos["y"]
        }

    def up(self):
        self.position["y"] += -1
    

    def down(self):
        self.position["y"] += 1
    

    def left(self):
        self.position["x"] += -1
    

    def right(self):
        self.position["x"] += 1