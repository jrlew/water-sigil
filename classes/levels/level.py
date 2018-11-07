"""
Placeholder
"""

class Level():
    def __init__(self, name, players, enemys, terrain, units):
        self.name = name
        self.players = players
        self.enemys = enemys
        self.terrain = terrain
        self.units = units
        for _player in players:
            self.units[_player.position.y][_player.position.x] = _player
        for _enemy in enemys:
            self.units[_enemy.position.y][_enemy.position.x] = _enemy
