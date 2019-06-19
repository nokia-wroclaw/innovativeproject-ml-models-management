import uuid
import json

from flask import jsonify, request
from flask_restful import Resource, reqparse, fields, abort
from flask_uploads import UploadSet
from flask_praetorian import auth_required, current_user

from app import db, models_uploadset
from app.models import Model, ModelSchema, ModelLesserSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse

from sqlalchemy.dialects.postgresql import array as postgres_array
from werkzeug.datastructures import FileStorage


class ModelAPI(Resource):
    method_decorators = [auth_required]

    def get(self, id: int) -> dict:
        """Returns data about a requested model.

        .. :quickref: Models; Get a single model.

        :param id: id of a requested model
        :returns: a single object
        """
        model = Model.query.filter_by(id=id).one_or_none()

        if not model:
            abort(404)

        return NestedResponse(schema=ModelSchema).dump(model)

    def delete(self, id: int) -> dict:
        """Removes a selected model.

        .. :quickref: Models; Delete a single model. 

        :param id: id of a requested model
        :returns: whether the operation has been successful
        """
        model = Model.query.filter_by(id=id).first()

        if not model:
            abort(404)

        db.session.delete(model)
        db.session.commit()

        return {"status": "success"}

    def put(self, id: int) -> dict:
        """Modifies a selected model.
        
        .. :quickref: Models; Update a single model. (Not implemented)

        :param id: id of the model to update
        :param payload: the data to override the model with
        :returns: the updated model
        """
        pass


class ModelListAPI(Resource):
    method_decorators = [auth_required]

    def get(self) -> list:
        """Lists all models that satisfy certain conditions.
        
        .. :quickref: Models; Get a collection of models.

        Every parameter can be appended multiple times.

        :param workspace: search for models only in this workspace
        :param project: search for models only in this project
        :param hyperparam: search for models that have this hyperparameter
        :param param: search for models that have this parameter
        :returns: a list of objects
        """
        parser = paginated_parser.copy()
        parser.add_argument("workspace", type=int)
        parser.add_argument("projects", type=str)
        parser.add_argument("hyperparameters", type=str)
        parser.add_argument("parameters", type=str)
        parser.add_argument("metrics", type=str)
        parser.add_argument("users", type=str)

        args = parser.parse_args()

        # Initialize query builder
        query = Model.query

        if args["workspace"]:
            # TODO: add fetching models from multiple workspaces
            # query = query.filter()
            pass
        if args["projects"]:
            query = query.filter(Model.project_id.in_(args["projects"].split(",")))
        if args["users"]:
            query = query.filter(Model.user_id.in_(args["users"].split(",")))
        # if args["hyperparameters"]:
        #     # Filtering through hyperparameters.
        #     # Every result has to contain ALL of the requested keys
        #     query = query.filter(
        #         Model.hyperparameters.has_all(
        #             postgres_array(args["hyperparameters"].split(","))
        #         )
        #     )
        # if args["parameters"]:
        #     # Filtering through parameters.
        #     # Every result has to contain ALL of the requested keys
        #     query = query.filter(
        #         Model.parameters.has_all(postgres_array(args["parameters"].split(",")))
        #     )
        if args["metrics"]:
            # Filtering through metrics.
            # Every result has to contain ALL of the requested keys
            query = query.filter(
                Model.metrics.has_all(postgres_array(args["metrics"].split(",")))
            )

        paginated_query = query.paginate(args["page"], args["per_page"], False)

        return NestedResponse(
            schema=ModelSchema,
            exclude=("parameters", "hyperparameters", "metrics"),
            many=True,
            pagination=paginated_query,
        ).dump(paginated_query.items)

    def post(self) -> dict:
        """Uploads a model.

        .. :quickref: Models; Upload a new model.

        :param name: human-readable name of the model
        :param dataset_name: name used to identify the dataset
        :param dataset_description: description used to provide more context
        :param project_id: id of the project the model belongs to
        :param hyperparameters: a dictionary of hyperparameters
        :param parameters: a dictionary of parameters
        :param metrics: a dictionary of metrics
        :param tags: a list of tags in form of a single string separated by commas
        :param git_active_branch: an active branch of the uploaded model
        :param git_commit_hash: hash of the most recent commit
        :param file: contents of the file selected to upload
        :param private: whether to mark the model as private
        :returns: a newly uploaded model
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("dataset_name", type=str)
        parser.add_argument("dataset_description", type=str)
        parser.add_argument("project_id", type=int, required=True)
        # user_id : deprecated
        parser.add_argument("user_id", type=int, required=False)
        parser.add_argument("hyperparameters", type=str, default="{}")
        parser.add_argument("parameters", type=str, default="{}")
        parser.add_argument("metrics", type=str, default="{}")
        parser.add_argument("tags", type=str, default="")
        parser.add_argument("git_active_branch", type=str, default=None)
        parser.add_argument("git_commit_hash", type=str, default=None)
        parser.add_argument("file", type=FileStorage, location="files", required=True)
        parser.add_argument("private", type=bool, default=False)
        args = parser.parse_args()

        if "file" in args:
            print("FILE:", args["file"])
            filename = models_uploadset.save(args["file"], name=str(uuid.uuid4()) + ".")

            for arg_name in ["hyperparameters", "parameters", "metrics"]:
                args[arg_name] = json.loads(args[arg_name])

            user = current_user()
            new_model = Model(
                user_id=user.id,
                project_id=args["project_id"],
                hyperparameters=args["hyperparameters"],
                parameters=args["parameters"],
                metrics=args["metrics"],
                name=args["name"],
                path=filename,
                dataset_name=args["dataset_name"],
                dataset_description=args["dataset_description"],
                git_active_branch=args["git_active_branch"],
                git_commit_hash=args["git_commit_hash"],
                private=args["private"],
            )

        db.session.add(new_model)
        db.session.commit()

        return NestedResponse(schema=ModelSchema).dump(new_model)


class ModelLesserListAPI(Resource):
    method_decorators = [auth_required]

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
        parser.add_argument("projects", type=str)

        args = parser.parse_args()

        # Initialize query builder
        query = Model.query

        paginated_query = query.paginate(args["page"], args["per_page"], False)

        return NestedResponse(
            schema=ModelLesserSchema, many=True, pagination=paginated_query
        ).dump(paginated_query.items)
