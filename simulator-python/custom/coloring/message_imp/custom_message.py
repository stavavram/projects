from core.message import Message

class MarkMessage(Message):
    def __init__(self, msg, path_root_id):
        self.msg = msg
        self.path_root_id = path_root_id
