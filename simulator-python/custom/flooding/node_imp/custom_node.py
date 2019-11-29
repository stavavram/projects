from core.node import Node
from core.utils.visualization_utils.color import (
    YELLOW
)
from core.runtime_engine import RunTimeEngine
from ..message_imp.custom_message import MarkMessage

class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.is_root = False
        self.parent = None

    def handle_messages(self):
        if self.is_root and RunTimeEngine.getInstance().rounds == 1:
            self.color = YELLOW
            self.broadcast(MarkMessage("hello world"))
        else:
            if self.parent is None and self.is_root is False:
                if self.inbox.has_next() is True:
                    self.color = YELLOW
                    msg = self.inbox.next()
                    self.parent = self.inbox.get_sender_of_active_packet().ID
                    print ("node:{} recieved msg".format(self.ID))
                    self.broadcast(msg)

    def print_neighbors(self):
        neighbors_array = []
        for neighbor in self.edges:
            neighbors_array.append(neighbor.end_node_id)
        print(neighbors_array)
