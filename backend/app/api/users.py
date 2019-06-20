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
        """Returns data about a requested user.

        .. :quickref: Users; Get a single user.

        :param id: id of a requested user
        :returns: a single object
        """
        user = User.query.filter_by(id=id).one_or_none()

        return NestedResponse(schema=UserSchema).dump(user)

    def delete(self, id: int) -> dict:
        """Removes a selected user.

        .. :quickref: Users; Delete a single user.

        :param id: id of a requested user
        :returns: whether the operation has been successful
        """
        user = User.query.filter_by(id=id).first()

        if not user:
            abort(404)

        db.session.delete(user)
        db.session.commit()

        return {"status": "success"}

    def put(self, id: int) -> dict:
        """Modifies a selected user.
        
        .. :quickref: Users; Update a single user. (Not implemented)

        :param id: id of the user to update
        :param payload: the data to override the user with
        :returns: the updated user
        """
        pass


class UserListAPI(Resource):
    method_decorators = [auth_required]

    def get(self) -> list:
        """Lists all users.
        
        .. :quickref: Users; Get a collection of users.

        :return: a list of users
        """
        parser = paginated_parser.copy()
        args = parser.parse_args()

        paginated_query = User.query.paginate(args["page"], args["per_page"], False)
        return NestedResponse(
            schema=UserSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        """Creates a new user.

        .. :quickref: Users; Create a new user.

        :param login: login for the new user
        :param password: password for the new user
        :param full_name: full name for the new user (optional)
        :param email: an email address for the new user (optional)
        :returns: a newly created user
        """
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
