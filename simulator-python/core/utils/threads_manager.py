from core.config.config import NUMBER_OF_THREADS
from core.utils.chunks_operations import split_to_chunks
from threading import Thread

def use_threads(func):
    def inner(*args, **kwargs):
        threads_list = []
        threads_num = int(NUMBER_OF_THREADS)
        collection = args[0]
        if threads_num > len(collection):
            threads_num = len(collection)
        chunks = list(split_to_chunks(collection, int(len(collection) / threads_num)))
        for chunk in chunks:
            thread = Thread(target=func, args=(chunk,))
            threads_list.append(thread)
            thread.start()
        for thread in threads_list:
            thread.join()
    return inner

