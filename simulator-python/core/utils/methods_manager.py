import re
import inspect

from core.config.config import SIMULATOR_NAME, BASE_PATH_FOR_IMPORT, REGEX_PROJECT_NAME
from core.storages.store_factory import StoreFactory
from core.config.config import KEY_VALUE_STORE_TYPE
from core.utils.parametrized import parametrized

store = StoreFactory.create_store(KEY_VALUE_STORE_TYPE)


@parametrized
def store_method(func, **kwargs):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("Error: " + str(e))
    project_name = re.sub(
        REGEX_PROJECT_NAME,
        '',
        func.__code__.co_filename.split(SIMULATOR_NAME)[1].split(BASE_PATH_FOR_IMPORT)[1]
    )
    method_name = func.__code__.co_name
    vars = inspect.getargspec(func).args
    if 'self' in vars:
        vars.remove('self')
    if 'cls' in vars:
        vars.remove('cls')
    parameters_info = {}
    for var in vars:
        description = ""
        if kwargs.get(var) is not None:
            description = kwargs.get(var)
        parameters_info[var] = {
            "description": description,
            "name": var
        }
    if store[project_name] is None:
        store[project_name] = StoreFactory.create_store(KEY_VALUE_STORE_TYPE)
    store[project_name][method_name] = parameters_info
    return inner


def convert_store_to_json(store_for_converting):
    if type(store_for_converting) in (int, float, bool, str):
        return store_for_converting
    if store_for_converting is not None:
        obj = {}
        keys = store_for_converting.keys()
        for key in keys:
            value = convert_store_to_json(store_for_converting[key])
            if value is not None:
                obj[key] = value
        return obj

