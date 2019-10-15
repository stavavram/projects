import jsons
import sys
from flask import Blueprint
from flask import Response
from core.runtime_engine import RunTimeEngine

nodes_api = Blueprint('nodes_api', __name__)

AMOUNT_LIMIT = 1000000
DEFAULT_AMOUNT = 300

@nodes_api.route('/get-nodes-data')
def get_nodes_data():
    nodes = RunTimeEngine.getInstance().get_nodes()
    if(sys.getsizeof(nodes) <= AMOUNT_LIMIT):
        return Response(jsons.dumps(nodes))
    return Response()