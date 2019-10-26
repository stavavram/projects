import jsons
import sys
from flask import Blueprint
from flask import Response
from core.runtime_engine import RunTimeEngine
from core.config.config import DEFAULT_NODES_AMOUNT

nodes_api = Blueprint('nodes_api', __name__)

@nodes_api.route('/get-nodes-data')
def get_nodes_data():
    nodes = RunTimeEngine.getInstance().get_nodes()
    if len(nodes) > DEFAULT_NODES_AMOUNT:
        return Response(jsons.dumps(nodes[:DEFAULT_NODES_AMOUNT]))
    return Response(jsons.dumps(nodes))