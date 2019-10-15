from core.utils.visualization_utils import color
from core.inbox import Inbox
from core.edge import Edge
from core.runtime_engine import RunTimeEngine
from core.packet import Packet
from core.storages.memory_store import MemoryStore

class Node:
    def __init__(self, id = None):
        if id is not None:
            self.ID = id
        else:
            self.ID = RunTimeEngine.getInstance().generate_node_id()
        self.store = MemoryStore()
        self.inbox = Inbox()
        self.edges = []
        self.color = color.BLACK

    def handle_messages(self):
        print("handle msg")

    def add_connection_to(self, node):
        edge_instance = Edge(self.ID, node.ID)
        self.edges.append(edge_instance)


    def broadcast(self, message, blacklist_ids = []):
        if self.store.get_from_storage(RunTimeEngine.getInstance().rounds) is None:
            self.store.add_to_storage(RunTimeEngine.getInstance().rounds, MemoryStore())
        for edge in self.edges:
            if edge.end_node_id in blacklist_ids:
                continue
            end_node = RunTimeEngine.getInstance().get_node_by_id(edge.end_node_id)
            msg_mapping_key = str(end_node.ID)
            if self.store.get_from_storage(RunTimeEngine.getInstance().rounds).get_from_storage(msg_mapping_key) is None:
                self.send(message, end_node)
                self.store.get_from_storage(RunTimeEngine.getInstance().rounds).add_to_storage(msg_mapping_key, True)

    def send(self, message, target):
        packet_instance = Packet(self.ID, target.ID, message)
        target.add_packet_to_inbox(packet_instance)

    def add_packet_to_inbox(self, packet):
        self.inbox.add_packet(packet)

    def init_registration_to_engine(self):
        RunTimeEngine.getInstance().init_node(self)

    def get_color(self):
        return self.color
