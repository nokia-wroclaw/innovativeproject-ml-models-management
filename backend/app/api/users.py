from flask import jsonify, request
from flask_restful import Resource

from app import db
from app.models import User
from app.api import paginated_parser


class UserAPI(Resource):
    def get(self, id: int) -> dict:
        pass

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class UserListAPI(Resource):
    def get(self) -> list:
        pass

    def post(self) -> dict:
        pass
