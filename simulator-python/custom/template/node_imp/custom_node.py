from core.node import Node
from core.utils.visualization_utils.color import (
    RED,
    YELLOW
)
from core.runtime_engine import RunTimeEngine
from ..message_imp.custom_message import MarkMessage

class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.is_root = False

    def handle_messages(self):
        if self.is_root and RunTimeEngine.getInstance().rounds == 1:
            self.color = RED
            self.broadcast(MarkMessage("hello world"))
        else:
            while(self.inbox.has_next()):
                self.color = YELLOW
                msg = self.inbox.next()
                print("round: {}, reciever: {}, sender: {}, msg: {}".
                      format(RunTimeEngine.getInstance().rounds, self.ID, self.inbox.get_sender_of_active_packet().ID, msg.msg))