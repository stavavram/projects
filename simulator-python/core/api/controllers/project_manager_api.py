import os
from os import listdir
from flask import (
    Blueprint,
    jsonify
)

from core.runtime_engine import RunTimeEngine

projects_api = Blueprint('projects_api', __name__)

BASE_PATH = "..\\..\\..\\custom\\"

@projects_api.route('/get-projects')
def get_projects():
    RunTimeEngine.getInstance().is_engine_active = False
    RunTimeEngine.getInstance().clean_nodes()
    RunTimeEngine.getInstance().rounds = 0
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),BASE_PATH)
    return jsonify(listdir(path))