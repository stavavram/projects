from core.node import Node
from core.utils.visualization_utils.color import (
    YELLOW,
    RED, GREEN)
from core.runtime_engine import RunTimeEngine
from ..message_imp.custom_message import MarkMessage

class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.is_root = False

    def handle_messages(self):
        if self.color is not YELLOW:
            if RunTimeEngine.getInstance().rounds == 1:
                print("node: {} starting".format(self.ID));
                self.color = RED;
                self.broadcast(MarkMessage("hello world"))
            else:
                while self.inbox.has_next() == True:
                    msg = self.inbox.next()
                    self.color = GREEN;
                    print("node: {} recieve msg from node: {}".format(self.ID, self.inbox.get_sender_of_active_packet().ID))
                    self.broadcast(msg, [self.inbox.get_sender_of_active_packet().ID]);


    def print_neighbors(self):
        neighbors_array = []
        for neighbor in self.edges:
            neighbors_array.append(neighbor.end_node_id)
        print(neighbors_array)
