from flask import jsonify, request, abort
from flask_restful import Resource, reqparse

from app import db
from app.models import Project, ProjectSchema, Workspace
from app.api import paginated_parser


class ProjectAPI(Resource):
    def get(self, id: int) -> dict:
        project = Project.query.filter_by(id=id).first()

        if not project:
            abort(404)

        return ProjectSchema().dump(project)

    def delete(self, id: int) -> dict:
        project = Project.query.filter_by(id=id).first()

        if not project:
            abort(404)

        db.session.delete(project)
        db.session.commit()

        return {"status": "success"}

    def put(self, id: int) -> dict:
        pass


class ProjectListAPI(Resource):
    def get(self) -> list:
        parser = paginated_parser.copy()
        args = parser.parse_args()
        projects = Project.query.paginate(args["page"], args["per_page"], False).items

        return ProjectSchema(many=True).dump(projects)

    def post(self) -> dict:
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

            return ProjectSchema().dump(project)
        return {"error": f"Workspace {args['workspace_id']} does not exist."}, 400
