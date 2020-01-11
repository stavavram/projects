import random

class GraphGenerator:
    @staticmethod
    def generate_direct_graph(nodes_num, node_class, edge_prob):
        return GraphGenerator.generate_graph_direct_or_not(nodes_num, node_class, edge_prob)

    @staticmethod
    def generate_graph(nodes_num, node_class, edge_prob):
        return GraphGenerator.generate_graph_direct_or_not(nodes_num, node_class, edge_prob, False)

    @staticmethod
    def generate_graph_direct_or_not(nodes_num, node_class, edge_prob, is_direct = True):
        nodes = GraphGenerator.create_nodes(nodes_num, node_class)
        for i in range(nodes_num):
            print(i)
            for j in range(nodes_num):
                if i!= j and  GraphGenerator.random(0, 100)/100 < edge_prob and (list(map(lambda edge: edge.end_node_id == nodes[j].ID, nodes[i].edges)).__contains__(True) is False):
                    nodes[i].add_connection_to(nodes[j])
                    if is_direct is False:
                        nodes[j].add_connection_to(nodes[i])
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

