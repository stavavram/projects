class ButtonsStorage:
    def __init__(self):
        self.storage = []

    def add_to_storage(self, button_meta_obj):
        self.storage.append(button_meta_obj)

    def get_storage(self):
        return self.storage
