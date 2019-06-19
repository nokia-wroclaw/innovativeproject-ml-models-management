from flask import jsonify, request, abort
from flask_restful import Resource, reqparse

from app import db
from app.models import Tag, Project, ProjectSchema, Workspace
from app.api import paginated_parser
from app.api.utils import NestedResponse


class ProjectAPI(Resource):
    def get(self, id: int) -> dict:
        """Returns data about a requested project.

        .. :quickref: Projects; Get a single project.
        
        :param id: id of a requested project
        :reqheader Authorization: Bearer JWT
        :status 200: when project exists
        :status 404: when requested project does not exist
        :returns: a single object
        """
        project = Project.query.filter_by(id=id).first()

        if not project:
            abort(404)

        return NestedResponse(schema=ProjectSchema).dump(project)

    def delete(self, id: int) -> dict:
        """Removes a selected project.

        .. :quickref: Projects; Delete a single project.

        :param id: id of a requested project
        :reqheader Authorization: Bearer JWT
        :status 200: when project exists and was deleted
        :status 404: when requested project does not exist
        :returns: whether the operation has been successful
        """
        project = Project.query.filter_by(id=id).first()

        if not project:
            abort(404)

        db.session.delete(project)
        db.session.commit()

        return {"status": "success"}

    def put(self, id: int) -> dict:
        """Modifies a selected project.
        
        .. :quickref: Projects; Update a single project. (Not implemented)

        :param id: id of the project to update
        :param payload: the data to override the project with
        :returns: the updated project
        """
        pass


class ProjectListAPI(Resource):
    def get(self) -> list:
        """Lists all projects.
        
        .. :quickref: Projects; Get a collection of projects.

        :param search: lists only projects that contain the name like `search`
        :return: a list of projects
        """
        parser = paginated_parser.copy()
        args = parser.parse_args()
        paginated_query = Project.query.paginate(args["page"], args["per_page"], False)

        return NestedResponse(
            schema=ProjectSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        """Creates a new project.

        .. :quickref: Projects; Create a new project.

        :param name: a name/title for the project
        :param description: a description of the project and it's purpose
        :param workspace_id: id of the workspace that contains this project
        :returns: a newly created project
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="No name provided")
        parser.add_argument("description", type=str)
        parser.add_argument("workspace_id", type=int, required=True)
        args = parser.parse_args()

        workspace = Workspace.query.filter_by(id=args["workspace_id"]).first()
        if workspace:
            project = Project(
                name=args["name"],
                description=args["description"],
                workspace_id=args["workspace_id"],
            )
            db.session.add(project)
            db.session.commit()

            return NestedResponse(schema=ProjectSchema).dump(project)
        return {"error": f"Workspace {args['workspace_id']} does not exist."}, 400
