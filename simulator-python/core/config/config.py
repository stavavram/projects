import platform
from core.storages.stores_keys import MEMORY_STORE

NUMBER_OF_THREADS = 6
KEY_VALUE_STORE_TYPE = MEMORY_STORE
REGEX_PROJECT_NAME = '[^A-Za-z0-9-_]+'
DEFAULT_NODES_AMOUNT = 250
if platform.system() == "Windows":
    BASE_PATH = "..\\..\\..\\custom\\"
else:
    BASE_PATH = "../../../custom/"
BASE_PATH = "..\\..\\..\\custom\\"
BASE_PATH_FOR_IMPORT = "custom"
SIMULATOR_NAME = "simulator-python"
