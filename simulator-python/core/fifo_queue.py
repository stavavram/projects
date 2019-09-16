from core.utils.jsonable import Jsonable

class FifoQueue:
    def __init__(self):
        self.queue = []

    def qsize(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def is_empty(self):
        if(self.qsize() == 0):
            return True
        return False
