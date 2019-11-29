from core.abstract_custom_global import AbstractCustomGlobal
from core.generators.graph_generator import GraphGenerator
from core.runtime_engine import RunTimeEngine
from core.utils.methods_manager import store_method
from .node_imp.custom_node import CustomNode
from core.utils.visualization_utils.color import YELLOW
import timeit

class CustomGlobal(AbstractCustomGlobal):
    round_duration = None
    start_duration = None
    nodes = []

    def main(self):
        """
        :return:
        """

    @store_method(nodes_count="The number of nodes", prob="probability of edge between 2 nodes")
    def build_graph(self, nodes_count, prob):
        nodes_count = int(nodes_count)
        prob = float(prob)
        nodes = GraphGenerator.generate_graph(nodes_count, CustomNode, prob)
        nodes[0].is_root = True
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
        #print("Round duration: {}".format(duration))
        max=0
        if self.check_if_finish() is True:
            total_dur = (timeit.default_timer() - self.start_duration)
            print("Finish! in duration:" + str(total_dur))

    def check_if_finish(self):
        for node in self.nodes:
            if node.get_color() is not YELLOW:
                return False
        return True

