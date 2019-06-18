import os
from flask import Blueprint, current_app
from flask_restful import Api, reqparse


# TODO: Replace environment variables with Flask internal  configuration dictionary
paginated_parser = reqparse.RequestParser()
paginated_parser.add_argument("page", type=int, default=1)
paginated_parser.add_argument("per_page", type=int, default=20)

from app.api.workspaces import WorkspaceAPI, WorkspaceListAPI
from app.api.projects import ProjectAPI, ProjectListAPI
from app.api.models import ModelAPI, ModelListAPI
from app.api.users import UserAPI, UserListAPI
from app.api.errors import errors
from app.api.auth import LoginAuthAPI, RefreshTokenAuthAPI

api_bp = Blueprint("api", __name__)
api = Api(api_bp, errors=errors)

api.add_resource(WorkspaceListAPI, "/workspaces/", endpoint="workspaces")
api.add_resource(WorkspaceAPI, "/workspaces/<int:id>/", endpoint="workspace")
api.add_resource(ProjectListAPI, "/projects/", endpoint="projects")
api.add_resource(ProjectAPI, "/projects/<int:id>/", endpoint="project")
api.add_resource(ModelListAPI, "/models/", endpoint="models")
api.add_resource(ModelAPI, "/models/<int:id>/", endpoint="model")
api.add_resource(UserListAPI, "/users/", endpoint="users")
api.add_resource(UserAPI, "/users/<int:id>/", endpoint="user")
api.add_resource(LoginAuthAPI, "/auth/login/", endpoint="login")
api.add_resource(RefreshTokenAuthAPI, "/auth/token/", endpoint="refresh_token")
