

class Edge:
    def __init__(self, start_node_id, end_node_id):
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.weight = 1

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

