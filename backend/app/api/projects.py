from flask import jsonify, request
from flask_restful import Resource

from app import db
from app.models import Project
from app.api import paginated_parser


class ProjectAPI(Resource):
    def get(self, id: int) -> dict:
        pass

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class ProjectListAPI(Resource):
    def get(self) -> list:
        pass

    def post(self) -> dict:
        pass
