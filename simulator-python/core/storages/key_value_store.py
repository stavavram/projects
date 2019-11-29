from collections.abc import Mapping

class KeyValueStore(Mapping):
    def __init__(self, *args, **kw):
        pass

    def __getitem__(self, key, *args, **kwargs):
        return self.get_from_storage(key)

    def __setitem__(self, key, value, *args, **kwargs):
        return self.add_to_storage(key, value)

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def keys(self):
        pass

    def add_to_storage(self, key, value, *args, **kwargs):
        pass

    def get_from_storage(self, key, *args, **kwargs):
        pass
