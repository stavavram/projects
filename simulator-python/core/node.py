from core.utils.visualization_utils import color
from core.inbox import Inbox
from core.edge import Edge
from core.runtime_engine import RunTimeEngine
from core.packet import Packet

class Node:
    def __init__(self, id = None):
        if id is not None:
            self.ID = id
        else:
            self.ID = RunTimeEngine.getInstance().get_node_id()

        self.inbox = Inbox()
        self.edges = []
        self.color = color.BLACK

    def handle_messages(self):
        print("handle msg")

    def add_connection_to(self, node):
        edge_instance = Edge(self.ID, node.ID)
        self.edges.append(edge_instance)


    def broadcast(self, message, blacklist_ids = []):
        for neighbor in self.edges:
            if blacklist_ids.__contains__(neighbor.end_node_id):
                continue
            end_node = RunTimeEngine.getInstance().get_node_by_id(neighbor.end_node_id)
            packet_instance = Packet(self.ID, end_node.ID, message)
            end_node.add_packet_to_inbox(packet_instance)


    def send(self, message, target):
        packet_instance = Packet(self.ID, target.ID, message)
        target.add_packet_to_inbox(packet_instance)


    def add_packet_to_inbox(self, packet):
        self.inbox.add_packet(packet)

    def init_registration_to_engine(self):
        RunTimeEngine.getInstance().init_node(self)
