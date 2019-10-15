from flask import (
    Blueprint,
    jsonify,
    Response,
    request
)
from core.runtime_engine import RunTimeEngine
from core.custom_global_manager import CustomGlobalManager

runtime_api = Blueprint('runtime_api', __name__)

BASE_PATH_FOR_IMPORT = "custom"

@runtime_api.route('/get-rounds')
def get_rounds():
    return jsonify(RunTimeEngine.getInstance().rounds)

@runtime_api.route('/invoke-main')
def invoke_main():
    project = request.args.get('project')
    if RunTimeEngine.getInstance().is_engine_active == False:
        module = __import__("{}.{}.custom_global".format(BASE_PATH_FOR_IMPORT, project))
        custom_class = getattr(getattr(getattr(module, project), "custom_global"), "CustomGlobal")
        instance = custom_class()
        CustomGlobalManager.set_custom_global(instance)
        instance.main()
    return Response()

@runtime_api.route('/invoke-method')
def invoke_method():
    project = request.args.get('project')
    method = request.args.get('method')
    if RunTimeEngine.getInstance().is_engine_active == False:
        module = __import__("{}.{}.custom_global".format(BASE_PATH_FOR_IMPORT, project))
        custom_class = getattr(getattr(getattr(module, project), "custom_global"), "CustomGlobal")
        instance = custom_class()
        method_to_call = getattr(instance, method)
        method_to_call()
    return Response()

@runtime_api.route('/stop')
def stop():
    RunTimeEngine.getInstance().stop_simulator()
    return Response()

@runtime_api.route('/run')
def run():
    RunTimeEngine.getInstance().run_simulator()
    return Response()

@runtime_api.route('/run-single-step')
def run_single_step():
    RunTimeEngine.getInstance().run_simulator_step()
    return Response()

