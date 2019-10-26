import random

from core.abstract_custom_global import AbstractCustomGlobal
from core.generators.graph_generator import GraphGenerator
from core.runtime_engine import RunTimeEngine
from .node_imp.custom_node import CustomNode
import timeit

class CustomGlobal(AbstractCustomGlobal):
    def main(self):
        self.build_tree(6, 15)

    def build_tree(self, max_degree, leaves_num):
        leaves = []
        for i in range(leaves_num):
            leave = CustomNode()
            leave.init_registration_to_engine()
            leaves.append(leave)

        level = 0
        child_pos_in_lvl = 0
        current_level_nodes = []
        prev_level_nodes = leaves

        while len(prev_level_nodes) > 1:
            node = CustomNode()
            node.init_registration_to_engine()
            degree = random.randint(1, max_degree)
            limit = degree if degree < len(prev_level_nodes) - child_pos_in_lvl else len(prev_level_nodes) - child_pos_in_lvl
            for i in range(limit):
                prev_level_nodes[child_pos_in_lvl].parent = node
                node.add_connection_to(prev_level_nodes[child_pos_in_lvl])
                node.childs.append(prev_level_nodes[child_pos_in_lvl])
                child_pos_in_lvl +=1
            current_level_nodes.append(node)
            if(child_pos_in_lvl == len(prev_level_nodes)):
                level +=1
                prev_level_nodes = current_level_nodes
                current_level_nodes = []
                child_pos_in_lvl = 0



