"""
Placeholder
"""


class Unit():
    def __init__(self, init_pos_tuple, stats_dict):
        self.position = Position(init_pos_tuple)
        self.prev_position = Position(init_pos_tuple)
        self.stats = Stats(stats_dict)
        # TODO: move/name this better
        # self.has_moved = False # Don't need this, use stats.remaining_movment instead

    def up(self):
        self.update_prev_position()
        self.position.y -= 1

    def down(self):
        self.update_prev_position()
        self.position.y += 1

    def left(self):
        self.update_prev_position()
        self.position.x -= 1

    def right(self):
        self.update_prev_position()
        self.position.x += 1

    def update_prev_position(self):
        self.prev_position.y = int(self.position.y)
        self.prev_position.x = int(self.position.x)


class Stats():
    def __init__(self, init_stats):
        self.name = init_stats["name"]
        self.max_hp = init_stats["hp"]
        self.current_hp = init_stats["hp"]
        self.strength = init_stats["strength"]
        self.defense = init_stats["defense"]
        self.accuracy = init_stats["accuracy"]
        self.evasion = init_stats["evasion"]
        # TODO: add these to unit init params
        self.movement = 1
        self.remaining_movement = 1


class Position():
    def __init__(self, pos_tuple):
        self.x = pos_tuple[0]
        self.y = pos_tuple[1] 
