from core.node import Node
from core.runtime_engine import RunTimeEngine
from ..message_imp.custom_message import MarkMessage

class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.parent_per_path_root_id = {}

    def handle_messages(self):
        if RunTimeEngine.getInstance().rounds == 1:
            print("node: {} starting".format(self.ID));
            self.broadcast(MarkMessage("", self.ID))
        else:
            while self.inbox.has_next() == True:
                msg = self.inbox.next()
                root_id = msg.path_root_id
                if self.parent_per_path_root_id.get(root_id) is None:
                    self.parent_per_path_root_id[root_id] = self.inbox.get_sender_of_active_packet().ID
                    print("node: {} recieve msg from node: {}".format(self.ID, self.inbox.get_sender_of_active_packet().ID))
                    self.broadcast(msg, [root_id, self.inbox.get_sender_of_active_packet().ID]);


    def get_neighbors(self):
        neighbors_array = []
        for neighbor in self.edges:
            neighbors_array.append(neighbor.end_node_id)
        return neighbors_array
