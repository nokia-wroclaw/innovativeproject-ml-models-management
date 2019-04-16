from flask import jsonify, request
from flask_restful import Resource, reqparse

from app import db, praetorian
from app.models import User, UserSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse


class LoginAuthAPI(Resource):
    def post(self):
        """Logs a user in by parsing a POST request containing user credentials and
        issuing a JWT token.
        
        .. example::
        
            $ curl http://localhost:5000/api/v1/auth/login/ -X POST \
                -d '{"login":"zofiakochutek","password":"clechay"}'
        """
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        args = parser.parse_args()

        user = praetorian.authenticate(args["login"], args["password"])
        response = {"access_token": praetorian.encode_jwt_token(user)}

        return NestedResponse().dump(response)


class RefreshTokenAuthAPI(Resource):
    def get(self):
        """Refreshes an existing JWT by creating a new one that is a copy of the old
        except that it has a refrehsed access expiration.
        
        .. example::
        
        $ curl http://localhost:5000/api/v1/auth/token/ -X GET \
            -H "Authorization: Bearer <your_token>"
        """
        old_token = praetorian.read_token_from_header()
        new_token = praetorian.refresh_jwt_token(old_token)

        response = {"access_token": new_token}

        return NestedResponse().dump(response)
