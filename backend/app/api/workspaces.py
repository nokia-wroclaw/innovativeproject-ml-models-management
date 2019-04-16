from flask import jsonify, request
from flask_restful import Resource, reqparse

from app import db
from app.models import Workspace, WorkspaceSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse


class WorkspaceAPI(Resource):
    def get(self, id: int) -> dict:
        workspace = Workspace.query.filter_by(id=id).first()

        if not workspace:
            abort(404)

        return NestedResponse(schema=WorkspaceSchema).dump(workspace)

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class WorkspaceListAPI(Resource):
    def get(self) -> list:
        parser = paginated_parser.copy()
        args = parser.parse_args()
        paginated_query = Workspace.query.paginate(
            args["page"], args["per_page"], False
        )

        return NestedResponse(
            schema=WorkspaceSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="No name provided")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        workspace = Workspace(name=args["name"], description=args["description"])
        db.session.add(workspace)
        db.session.commit()

        return NestedResponse(schema=WorkspaceSchema).dump(workspace)

