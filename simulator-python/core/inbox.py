from core.fifo_queue import FifoQueue
from core.runtime_engine import RunTimeEngine

class Inbox:
    def __init__(self):
        self.packets_queue = FifoQueue()
        self.active_packet = None

    def add_packet(self, packet):
        packet.available_in_round = RunTimeEngine.getInstance().get_rounds() + 1
        self.packets_queue.enqueue(packet)

    def has_next(self):
        if self.packets_queue.is_empty() == False and self.packets_queue.top().available_in_round == RunTimeEngine.getInstance().get_rounds():
            return True
        return False

    def next(self):
        if(self.has_next()):
            self.active_packet = self.packets_queue.dequeue()
            return self.active_packet.message
        else:
            raise Exception("packetArray out of the range")

    def size(self):
        return self.packets_queue.qsize()

    def get_sender_of_active_packet(self):
        if(self.active_packet != None):
            return RunTimeEngine.getInstance().get_node_by_id(self.active_packet.source_id);
        else:
            raise Exception("Active Packet does not exists")

    def get_receiver_of_active_packet(self):
        if(self.active_packet != None):
            return RunTimeEngine.getInstance().get_node_by_id(self.active_packet.destination_id);
        else:
            raise Exception("Active Packet does not exists")
