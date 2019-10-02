from core.generators.graph_generator import GraphGenerator
from .node_imp.custom_node import CustomNode

class CustomGlobal:
    def main(self):
        nodes = GraphGenerator.generate_graph(20, CustomNode, 0.1)
        nodes[0].is_root = True