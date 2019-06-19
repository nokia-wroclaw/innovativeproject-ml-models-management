from flask import jsonify, request
from flask_restful import Resource, reqparse

from app import db
from app.models import Workspace, WorkspaceSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse


class WorkspaceAPI(Resource):
    def get(self, id: int) -> dict:
        """Returns data about a requested workspace.

        .. :quickref: Workspaces; Get a single workspace.

        :param id: id of a requested workspace
        :returns: a single object
        """
        workspace = Workspace.query.filter_by(id=id).first()

        if not workspace:
            abort(404)

        return NestedResponse(schema=WorkspaceSchema).dump(workspace)

    def delete(self, id: int) -> dict:
        """Removes a selected workspace.

        .. :quickref: Workspaces; Delete a single workspace.

        :param id: id of a requested workspace
        :returns: whether the operation has been successful
        """
        workspace = Workspace.query.filter_by(id=id).first()

        if not workspace:
            abort(404)

        db.session.delete(workspace)
        db.session.commit()

        return {"status": "success"}

    def put(self, id: int) -> dict:
        """Modifies a selected workspace.
        
        .. :quickref: Workspaces; Update a single workspace. (Not implemented)

        :param id: id of the workspace to update
        :param payload: the data to override the workspace with
        :returns: the updated project
        """
        pass


class WorkspaceListAPI(Resource):
    def get(self) -> list:
        """Lists all workspaces.
        
        .. :quickref: Workspaces; Get a collection of workspaces.

        :param search: lists only workspaces that contain the name like `search`
        :return: a list of workspaces
        """
        parser = paginated_parser.copy()
        args = parser.parse_args()
        paginated_query = Workspace.query.paginate(
            args["page"], args["per_page"], False
        )

        return NestedResponse(
            schema=WorkspaceSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        """Creates a new workspaces.

        .. :quickref: Workspaces; Create a new workspace.

        :param name: a name/title for the workspace
        :param description: a description of the workspace and it's purpose
        :returns: a newly created workspace
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="No name provided")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        workspace = Workspace(name=args["name"], description=args["description"])
        db.session.add(workspace)
        db.session.commit()

        return NestedResponse(schema=WorkspaceSchema).dump(workspace)
