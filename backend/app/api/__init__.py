import os
from flask import Blueprint, current_app
from flask_restful import Api, reqparse


# TODO: Replace environment variables with Flask internal  configuration dictionary
paginated_parser = reqparse.RequestParser()
paginated_parser.add_argument("page", type=int, default=1)
paginated_parser.add_argument("per_page", type=int, default=20)

from app.api.workspaces import WorkspaceAPI, WorkspaceListAPI
from app.api.projects import ProjectAPI, ProjectListAPI
from app.api.models import ModelAPI, ModelListAPI, ModelLesserListAPI
from app.api.users import UserAPI, UserListAPI
from app.api.tags import TagAPI, TagListAPI
from app.api.errors import errors
from app.api.auth import LoginAuthAPI, RefreshTokenAuthAPI
from app.api.model_tag_assoc import ModelTagAssocAPI

api_bp = Blueprint("api", __name__)
api = Api(api_bp, errors=errors)

api.add_resource(WorkspaceListAPI, "/workspaces/", endpoint="workspaces")
api.add_resource(WorkspaceAPI, "/workspaces/<int:id>/", endpoint="workspace")
api.add_resource(ProjectListAPI, "/projects/", endpoint="projects")
api.add_resource(ProjectAPI, "/projects/<int:id>/", endpoint="project")
api.add_resource(ModelListAPI, "/models/", endpoint="models")
# api.add_resource(ModelLesserListAPI, "/lesser/models/")
api.add_resource(ModelAPI, "/models/<int:id>/", endpoint="model")
api.add_resource(ModelTagAssocAPI, "/models/<int:model_id>/tags/<int:tag_id>/")
api.add_resource(UserListAPI, "/users/", endpoint="users")
api.add_resource(UserAPI, "/users/<int:id>/", endpoint="user")
api.add_resource(TagListAPI, "/tags/", endpoint="tags")
api.add_resource(TagAPI, "/tags/<int:id>/", endpoint="tag")
api.add_resource(LoginAuthAPI, "/auth/login/", endpoint="login")
api.add_resource(RefreshTokenAuthAPI, "/auth/token/", endpoint="refresh_token")
