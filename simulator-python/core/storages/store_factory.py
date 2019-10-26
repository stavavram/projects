from core.storages.memory_store import MemoryStore
from core.storages.stores_keys import MEMORY_STORE

class StoreFactory:
    supported_stores = {
        MEMORY_STORE: MemoryStore
    }

    @classmethod
    def create_store(cls, store_key):
        if cls.supported_stores.get(store_key) is not None:
            return cls.supported_stores[store_key]()
        raise Exception("Store does not exist")
