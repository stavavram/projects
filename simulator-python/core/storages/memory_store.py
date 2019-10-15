from core.storages.key_value_store import KeyValueStore

class MemoryStore(KeyValueStore):
    def __init__(self):
        self.storage = {}

    def add_to_storage(self, key, value):
        self.storage[key] = value

    def get_from_storage(self, key):
        if key in self.storage.keys():
            return self.storage[key]
        return None
