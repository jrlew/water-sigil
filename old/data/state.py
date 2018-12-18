"""
Placeholder
"""


class State():
    def __init__(self, screen, level, indicator):
        self.flags = Flags()
        self.screen = screen
        self.level = level
        self.indicator = indicator


class Flags():
    def __init__(self):
        self.player_turn = True
        self.update = False
        self.player_moving = False
        self.attack_prompt = False
        self.player_won = False