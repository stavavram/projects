import jsons
import json
from flask import (
    Blueprint,
    jsonify,
    Response,
    request
)
from core.config.config import BASE_PATH_FOR_IMPORT
from core.runtime_engine import RunTimeEngine
from core.custom_global_manager import CustomGlobalManager
from core.utils.methods_manager import store, convert_store_to_json
from core.utils.global_vars import set_project_value, get_project_value

runtime_api = Blueprint('runtime_api', __name__)

@runtime_api.route('/get-rounds')
def get_rounds():
    return jsonify(RunTimeEngine.getInstance().rounds)

@runtime_api.route('/invoke-main')
def invoke_main():
    project = request.args.get('project')
    if get_project_value() != project:
        RunTimeEngine.getInstance().disactivate_engine()
        RunTimeEngine.getInstance().clean_nodes()
        RunTimeEngine.getInstance().rounds = 0
    if RunTimeEngine.getInstance().is_engine_active() is False:
        set_project_value(project)
        RunTimeEngine.getInstance().activate_engine()
        module = __import__("{}.{}.custom_global".format(BASE_PATH_FOR_IMPORT, project))
        custom_class = getattr(getattr(getattr(module, project), "custom_global"), "CustomGlobal")
        instance = custom_class()
        CustomGlobalManager.set_custom_global(instance)
        instance.main()
        methods = convert_store_to_json(store[project])
        if methods is None:
            return Response()
        return Response(jsons.dumps(methods))
    return Response(jsons.dumps("The engine is already activated."),
                    status=400)


@runtime_api.route('/invoke-method', methods=['POST'])
def invoke_method():
    if RunTimeEngine.getInstance().is_engine_active() is True:
        data = json.loads(request.get_data().decode('utf8').replace("'", '"'))
        project = data.get('project')
        method = data.get('method')
        del data['project']
        del data['method']
        module = __import__("{}.{}.custom_global".format(BASE_PATH_FOR_IMPORT, project))
        custom_class = getattr(getattr(getattr(module, project), "custom_global"), "CustomGlobal")
        instance = custom_class()
        method_to_call = getattr(instance, method)
        method_to_call(**data)
        return Response(jsons.dumps("success"),200)
    else:
        print("The engine is not working. please choose a project and run the main function")
        return Response(jsons.dumps("The engine is not working. please choose a project and run the main function"), status=400)

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

