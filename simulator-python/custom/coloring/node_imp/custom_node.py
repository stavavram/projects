from core.node import Node
from core.runtime_engine import RunTimeEngine
import random

class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.graph_delta = 0
        self.colors_mapping = self.generate_colors()

    def handle_messages(self):
        if self.is_different_from_neighbors(self.get_color()) is False:
            if random.random() <= 0.5:
                new_color = random.randint(1, self.graph_delta + 1)
                if self.is_different_from_neighbors(new_color):
                    self.color = self.colors_mapping[new_color]

    def get_neighbors(self):
        neighbors_array = []
        for neighbor in self.edges:
            neighbors_array.append(neighbor)
        return neighbors_array

    def is_different_from_neighbors(self, color):
        neighbors_array = self.get_neighbors();
        colors = list(map(lambda neighbor: RunTimeEngine.getInstance().get_node_by_id(neighbor.end_node_id).get_color(), neighbors_array))
        if color in colors:
            return False;
        return True;

    def generate_colors(self):
        colors_mapping = {}
        for i in range(self.graph_delta + 10):
            r = lambda: random.randint(0, 255)
            colors_mapping[i] = '#%02X%02X%02X' % (r(), r(), r())
        return colors_mapping