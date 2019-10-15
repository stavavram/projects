from core.generators.graph_generator import GraphGenerator
from core.abstract_custom_global import AbstractCustomGlobal
from .node_imp.custom_node import CustomNode
import timeit

class CustomGlobal(AbstractCustomGlobal):
    duration = None
    nodes = []

    def main(self):
        nodes = GraphGenerator.generate_graph(10, CustomNode, 0.2)
        max = 0
        for node in nodes:
            if len(node.edges) > max:
                max = len(node.edges)
        print("delta is: " + str(max))

        for node in nodes:
            node.graph_delta = max
        self.nodes = nodes

    def pre_round(self):
        self.duration = timeit.default_timer()

    def post_round(self):
        duration = timeit.default_timer() - self.duration
        print("Round duration: {}".format(duration))
        max=0
        for node in self.nodes:
            if node.inbox.size() > max:
                max = node.inbox.size()
        print("Max inbox queue size is: {}".format(max))

        for node in self.nodes:
            if node.is_different_from_neighbors(node.get_color()) == False:
                return;
        print("Finish!!!!")

