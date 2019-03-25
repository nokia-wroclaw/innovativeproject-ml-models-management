from flask import jsonify, request
from flask_restful import Resource

from app import db
from app.models import Workspace
from app.api import paginated_parser


class WorkspaceAPI(Resource):
    def get(self, id: int) -> dict:
        pass

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class WorkspaceListAPI(Resource):
    def get(self) -> list:
        pass

    def post(self) -> dict:
        pass
