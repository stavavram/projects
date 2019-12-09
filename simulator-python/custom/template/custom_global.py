from core.abstract_custom_global import AbstractCustomGlobal
from core.generators.graph_generator import GraphGenerator
from .node_imp.custom_node import CustomNode

class CustomGlobal(AbstractCustomGlobal):
    def main(self):
        nodes = GraphGenerator.generate_graph(30, CustomNode, 0.01)
        nodes[0].is_root = True