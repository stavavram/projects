from core.storages.key_value_store import KeyValueStore


class MemoryStore(KeyValueStore):
    def __init__(self):
        self._storage = {}

    def keys(self):
        return self._storage.keys()

    def __iter__(self):
        return iter(self._storage)

    def add_to_storage(self, key, value, *args, **kwargs):
        self._storage[key] = value

    def get_from_storage(self, key, *args, **kwargs):
        return self._storage.get(key)
