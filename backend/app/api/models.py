from flask import jsonify, request
from flask_restful import Resource, reqparse, fields, abort

from app import db
from app.models import Model, ModelSchema
from app.api import paginated_parser

from sqlalchemy.dialects.postgresql import array as postgres_array


class ModelAPI(Resource):
    def get(self, id: int) -> dict:
        """Returns data about a requested model.
        
        :param id: id of a requested model
        :returns: a single object
        """
        model = Model.query.filter_by(id=id).first()

        if not model:
            abort(404)

        return ModelSchema().dump(model)

    def delete(self, id: int) -> dict:
        """Removes a selected model.

        :param id: id of a requested model
        :returns: whether the operation has been successful
        """
        pass

    def put(self, id: int) -> dict:
        """Modifies a selected model.
        
        :param id: id of the model to update
        :param payload: the data to override the model's with
        :returns: the updated model object
        """
        pass


class ModelListAPI(Resource):
    def get(self) -> list:
        """Lists all models that satisfy certain conditions.
        
        Every parameter can be appeneded multiple times.
        :param workspace: search for models only in this workspace
        :param project: search for models only in this project
        :param hyperparam: search for models that have this hyperparameter
        :param param: search for models that have this parameter

        :returns: a list of objects
        """
        parser = paginated_parser.copy()
        parser.add_argument("workspace", type=int, action="append")
        parser.add_argument("project", type=int, action="append")
        parser.add_argument("hyperparam", type=str, action="append")
        parser.add_argument("param", type=str, action="append")
        args = parser.parse_args()

        # Initialize query builder
        query = Model.query

        if args["workspace"]:
            # TODO: add fetching models from multiple workspaces
            # query = query.filter()
            pass
        if args["project"]:
            # TODO: add fetching models from multiple projects
            # query = query.filter()
            pass
        if args["hyperparam"]:
            # Filtering through hyperparameters.
            # Every result has to contain ALL of the requested keys
            query = query.filter(
                Model.hyperparameters.has_all(postgres_array(args["hyperparam"]))
            )
        if args["param"]:
            # Filtering through parameters.
            # Every result has to contain ALL of the requested keys
            query = query.filter(
                Model.parameters.has_all(postgres_array(args["param"]))
            )

        return ModelSchema(many=True).dump(
            query.paginate(args["page"], args["per_page"], False).items
        )

    def post(self) -> dict:
        pass
