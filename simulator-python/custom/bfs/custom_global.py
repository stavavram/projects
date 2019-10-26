from core.generators.graph_generator import GraphGenerator
from core.abstract_custom_global import AbstractCustomGlobal
from .node_imp.custom_node import CustomNode
from core.runtime_engine import RunTimeEngine
import timeit

class CustomGlobal(AbstractCustomGlobal):
    duration = None
    start_duration = None
    nodes = []

    def main(self):
        nodes = GraphGenerator.generate_graph(100, CustomNode, 0.08)
        max = 0
        for node in nodes:
            if len(node.edges) > max:
                max = len(node.edges)
        print("delta is: " + str(max))
        self.nodes = nodes

    def pre_round(self):
        self.duration = timeit.default_timer()
        if RunTimeEngine.getInstance().rounds == 0:
            self.start_duration = timeit.default_timer()

    def post_round(self):
        duration = timeit.default_timer() - self.duration
        print("Round duration: {}".format(duration))
        for node in self.nodes:
            if len(node.finish_for_root_ids) < len(self.nodes)-1:
                return;
        total_dur = (timeit.default_timer() - self.start_duration)
        print("total duration:" + str(total_dur))
        print("Round: {}".format(RunTimeEngine.getInstance().rounds))
        exit()

