from flask import jsonify, request
from flask_restful import Resource, reqparse

from app import db
from app.models import Workspace, WorkspaceSchema
from app.api import paginated_parser


class WorkspaceAPI(Resource):
    def get(self, id: int) -> dict:
        workspace = Workspace.query.filter_by(id=id).first()

        return WorkspaceSchema().dump(workspace)

    def delete(self, id: int) -> dict:
        pass

    def put(self, id: int) -> dict:
        pass


class WorkspaceListAPI(Resource):
    def get(self) -> list:
        parser = paginated_parser.copy()
        args = parser.parse_args()

        return WorkspaceSchema(many=True).dump(
            Workspace.query.paginate(args["page"], args["per_page"], False).items
        )

    def post(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="No name provided", location="json"
        )
        parser.add_argument("description", type=str, default="", location="json")
        args = parser.parse_args()
        workspace = Workspace(name=args["name"], description=args["description"])
        db.session.add(workspace)
        db.session.commit()

        return WorkspaceSchema().dump(workspace)
