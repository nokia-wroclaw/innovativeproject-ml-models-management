from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_praetorian import auth_required, current_user

from app.api import current_app
from app import db, praetorian
from app.models import User, UserSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse


class LoginAuthAPI(Resource):
    def post(self):
        """Logs the user in by parsing a POST request containing user credentials and
        issuing a JWT token.

        .. :quickref: Authentication; Log user in.

        .. code-block:: bash
        
            $ curl http://localhost:5000/api/v1/auth/login/ -X POST \\
              -d '{"login":"zofiakochutek", "password":"clechay"}'
        """
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        args = parser.parse_args()

        user = praetorian.authenticate(args["login"], args["password"])
        current_app.logger.info("user " + str(user.id) + " logged in successfully")
        response = {
            "access_token": praetorian.encode_jwt_token(user),
            "valid_for": praetorian.access_lifespan.total_seconds(),
            "user": {
                "id": user.id,
                "login": user.login,
                "full_name": user.full_name,
                "email": user.email,
            },
        }

        return NestedResponse().dump(response)


class RefreshTokenAuthAPI(Resource):
    method_decorators = [auth_required]

    def get(self):
        """Refreshes an existing JWT by creating a new one that is a copy of the old
        except that it has a refreshed access expiration.
        
        .. :quickref: Authentication; Refresh a token.

        .. code-block:: bash

            $ curl http://localhost:5000/api/v1/auth/token/ -X GET \\
              -H "Authorization: Bearer <your_token>"
        """
        # old_token = praetorian.read_token_from_header()
        # new_token = praetorian.refresh_jwt_token(old_token)
        # response = {"access_token": new_token}

        user = current_user()
        response = {
            "access_token": praetorian.encode_jwt_token(user),
            "valid_for": praetorian.access_lifespan.total_seconds(),
            "user": {
                "id": user.id,
                "login": user.login,
                "full_name": user.full_name,
                "email": user.email,
            },
        }

        return NestedResponse().dump(response)
