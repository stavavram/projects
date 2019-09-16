from flask_cors import CORS
from flask import (
    Flask
)
from core.api.controllers.node_api import nodes_api
from core.api.controllers.project_manager_api import projects_api
from core.api.controllers.runtime_api import runtime_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(nodes_api)
app.register_blueprint(projects_api)
app.register_blueprint(runtime_api)






