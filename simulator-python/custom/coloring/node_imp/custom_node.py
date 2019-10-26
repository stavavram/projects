from core.node import Node
from core.runtime_engine import RunTimeEngine
import random

colors_mapping = {}

def generate_colors(delta):
    for i in range(delta + 5):
        r = lambda: random.randint(0, 255)
        colors_mapping[i] = '#%02X%02X%02X' % (r(), r(), r())

class CustomNode(Node):
    graph_delta = 0

    def __init__(self):
        Node.__init__(self)

    def handle_messages(self):
        if self.is_different_from_neighbors(self.get_color()) is False:
            if random.random() <= 0.5:
                new_color = random.randint(1, self.graph_delta + 1)
                if self.is_different_from_neighbors(new_color):
                    self.color = colors_mapping[new_color]

    def get_neighbors(self):
        neighbors_array = []
        for neighbor in self.edges:
            neighbors_array.append(neighbor.end_node_id)
        return neighbors_array

    def is_different_from_neighbors(self, color):
        neighbors_array = self.get_neighbors();
        get_color_from_nodes = lambda neighbor: RunTimeEngine.getInstance().get_node_by_id(neighbor).get_color()
        neighbors_colors_map = map(get_color_from_nodes, neighbors_array)
        colors = list(neighbors_colors_map)
        if color in colors:
            return False;
        return True;


