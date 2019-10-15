from core.abstract_custom_global import AbstractCustomGlobal

class CustomGlobalManager:
    custom_global = None

    @classmethod
    def get_custom_global(cls):
        return cls.custom_global

    @classmethod
    def set_custom_global(cls, custom_global_instance = None):
        if custom_global_instance is None:
            cls.custom_global = AbstractCustomGlobal()
        else:
            cls.custom_global = custom_global_instance
