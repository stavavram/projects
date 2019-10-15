def split_to_chunks(list, chunks_number):
    for i in range(0, len(list), chunks_number):
        yield list[i:i + chunks_number]