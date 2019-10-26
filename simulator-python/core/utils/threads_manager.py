from core.config.config import NUMBER_OF_THREADS
from core.utils.chunks_operations import split_to_chunks
from threading import Thread

def collect_active_threads(threads):
    for thread in threads:
        thread.join()

def get_threads_num(collection):
    threads_num = int(NUMBER_OF_THREADS)
    if threads_num > len(collection):
        threads_num = len(collection)
    return threads_num

def use_threads(func):
    def inner(*args, **kwargs):
        threads_list = []
        collection = args[0]
        chunks = list(split_to_chunks(collection, int(len(collection) / get_threads_num(collection))))
        for chunk in chunks:
            thread = Thread(target=func, args=(chunk,))
            threads_list.append(thread)
            thread.start()
        collect_active_threads(threads_list)
    return inner

