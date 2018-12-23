class Node():
    def __init__(self, parent, pos, mov, terrain_map):
        self.terrain_map = terrain_map
        self.parent = parent
        self.position = pos
        self.remaining_movement = mov
        self.children = self.get_children(terrain_map)
        

    # TODO: Simplify this
    def get_children(self, terrain_map):
        if self.remaining_movement:
            arr = []
            if not self.position[0] - 1 < 0:
                if (self.remaining_movement - self.terrain_map[self.position[1]][self.position[0] - 1].movement_cost):
                    arr.append(Node(self, (self.position[0] - 1, self.position[1]), self.remaining_movement - self.terrain_map[self.position[1]][self.position[0] - 1].movement_cost, terrain_map))

            if not self.position[0] + 1 > 9:
                if (self.remaining_movement - self.terrain_map[self.position[1]][self.position[0] + 1].movement_cost):
                    arr.append(Node(self, (self.position[0] + 1, self.position[1]), self.remaining_movement - self.terrain_map[self.position[1]][self.position[0] + 1].movement_cost, terrain_map))

            if not self.position[1] - 1 < 0 :
                if (self.remaining_movement - self.terrain_map[self.position[1] - 1][self.position[0]].movement_cost):
                    arr.append(Node(self, (self.position[0], self.position[1] - 1), self.remaining_movement - self.terrain_map[self.position[1] - 1 ][self.position[0]].movement_cost, terrain_map))

            if not self.position[1] + 1 > 9:
                if (self.remaining_movement - self.terrain_map[self.position[1] + 1][self.position[0]].movement_cost):
                    arr.append(Node(self, (self.position[0], self.position[1] + 1), self.remaining_movement - self.terrain_map[self.position[1] + 1][self.position[0]].movement_cost, terrain_map))
            return arr
        else:
            return []


def valid_node(node, closed_set, lower_bounds, upper_bounds):
    return (node.position[0] >= lower_bounds and
            node.position[1] >= lower_bounds and
            node.position[0] <= upper_bounds and
            node.position[1] <= upper_bounds and
            not node.position in closed_set)

# TODO: Name this better, add in terrain movement cost, use persist to grab min/max, fix inital movement value hack
def bfs(persist, start, movement, min, max):
    current_depth = []
    next_depth = []
    closed_set = set()

    # IDK why it needs + 1, probably should figure that out...
    current_depth.append(Node(None, start, movement + 1, persist.terrain))

    while True:
        current_node = current_depth.pop(0)

        for node in current_node.children:
            if valid_node(node, closed_set, min, max):
                next_depth.append(node)
                closed_set.add(node.position)

        if not current_depth:
            if not next_depth:
                break
            else:
                current_depth = next_depth
                next_depth = []
    
    return closed_set
