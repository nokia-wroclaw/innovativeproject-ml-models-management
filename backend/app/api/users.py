from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_praetorian import auth_required

from app import db
from app.models import User, UserSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse


class UserAPI(Resource):
    method_decorators = [auth_required]

    def get(self, id: int) -> dict:
        user = User.query.filter_by(id=id).one_or_none()

        return NestedResponse(schema=UserSchema).dump(user)

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class UserListAPI(Resource):
    method_decorators = [auth_required]

    def get(self) -> list:
        parser = paginated_parser.copy()
        args = parser.parse_args()

        paginated_query = User.query.paginate(args["page"], args["per_page"], False)
        return NestedResponse(
            schema=UserSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        parser.add_argument("full_name", type=str)
        parser.add_argument("email", type=str)
        args = parser.parse_args()

        new_user = User(
            login=args["login"],
            password=args["password"],
            full_name=args["full_name"],
            email=args["email"],
        )

        db.session.add(new_user)
        db.session.commit()

        return NestedResponse(schema=UserSchema).dump(new_user)
