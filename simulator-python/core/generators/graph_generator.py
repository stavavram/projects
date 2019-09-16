import random

class GraphGenerator:
    @staticmethod
    def generate_graph(nodes_num, node_class, edge_prob):
        nodes = GraphGenerator.create_nodes(nodes_num, node_class)
        for i in range(nodes_num):
            for j in range(nodes_num):
                if(i!= j and GraphGenerator.random(0, 100)/100 <= edge_prob):
                    nodes[i].add_connection_to(nodes[j])
        return nodes

    @staticmethod
    def create_nodes(nodes_num, node_class):
        nodes = []
        for i in range(nodes_num):
            node = node_class()
            node.init_registration_to_engine()
            nodes.append(node)
        return nodes

    @staticmethod
    def random(min, max):
        return random.randrange(min, max)

