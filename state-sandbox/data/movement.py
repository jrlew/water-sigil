class Node():
    def __init__(self, parent, pos, mov):
        self.parent = parent
        self.position = pos
        # Initial call needs movement + start terrain mod to offset value
        self.remaining_movement = mov - 1
        self.children = self.get_children()

    def get_children(self):
        if self.remaining_movement:
            return [
                Node(
                    self, (self.position[0] - 1, self.position[1]), self.remaining_movement),
                Node(
                    self, (self.position[0] + 1, self.position[1]), self.remaining_movement),
                Node(
                    self, (self.position[0], self.position[1] - 1), self.remaining_movement),
                Node(
                    self, (self.position[0], self.position[1] + 1), self.remaining_movement),
            ]
        else:
            return []


def valid_node(node, closed_set, lower_bounds, upper_bounds):
    return (node.position[0] >= lower_bounds and
            node.position[1] >= lower_bounds and
            node.position[0] <= upper_bounds and
            node.position[1] <= upper_bounds and
            not node.position in closed_set)

# TODO: Name this better, add in terrain movement cost, use persist to grab min/max, fix inital movement value hack
def bfs(start, movement, min, max):
    current_depth = []
    next_depth = []
    closed_set = set()

    # Initial call needs movement + start terrain mod to offset value
    current_depth.append(Node(None, start, movement + 1))

    while True:
        current_node = current_depth.pop(0)

        for node in current_node.get_children():
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