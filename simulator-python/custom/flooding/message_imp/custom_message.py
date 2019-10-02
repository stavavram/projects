from core.message import Message

class MarkMessage(Message):
    def __init__(self, msg):
        self.msg = msg
