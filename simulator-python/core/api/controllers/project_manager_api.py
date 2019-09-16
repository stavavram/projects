import os
from os import listdir
from flask import (
    Blueprint,
    jsonify
)

projects_api = Blueprint('projects_api', __name__)

BASE_PATH = "..\\..\\..\\custom\\"

@projects_api.route('/get-projects')
def get_projects():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),BASE_PATH)
    return jsonify(listdir(path))