class Packet:
    def __init__(self, source_id, destination_id, message):
        self.destination_id = destination_id
        self.source_id = source_id
        self.message = message
        self.available_in_round = 0

    def activate_from_round(self, round):
        self.available_in_round = round