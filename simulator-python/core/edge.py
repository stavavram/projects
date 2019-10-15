

class Edge:
    def __init__(self, start_node_id, end_node_id):
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.weight = 1
        self.number_of_messages_on_this_edge = 0

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_number_of_messages_on_this_edge(self):
        return self.number_of_messages_on_this_edge

    def add_number_of_messages_on_this_edge(self):
        self.number_of_messages_on_this_edge += 1
