from core.node import Node
from core.utils.visualization_utils.color import (
    YELLOW,
    BLACK, BLUE, RED)
from custom.colors_test.message_imp.custom_message import MarkMessage


class CustomNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.base_color = BLACK
        self.color_A = YELLOW
        self.color_B = BLUE
        self.root_color = RED
        self.childs = []
        self.parent = None

    def handle_messages(self):
        if self.get_color() == self.base_color:
            if self.parent is None:
                self.color = self.root_color
                self.broadcast(MarkMessage(self.color_A))
            elif self.inbox.has_next():
                msg = self.inbox.next()
                self.color = msg.msg
                color_for_sending = self.color_B if msg.msg == self.color_A else self.color_A
                self.broadcast(MarkMessage(color_for_sending))


