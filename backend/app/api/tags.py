import uuid
import json

from flask import jsonify, request
from flask_restful import Resource, reqparse, fields, abort
from flask_uploads import UploadSet
from flask_praetorian import auth_required

from app import db
from app.models import Tag, TagSchema
from app.api import paginated_parser
from app.api.utils import NestedResponse

from sqlalchemy.dialects.postgresql import array as postgres_array
from werkzeug.datastructures import FileStorage


class TagAPI(Resource):
    method_decorators = [auth_required]

    def get(self, id: int) -> dict:
        """Returns data about a requested tag.
        
        :param id: id of a requested tag
        :returns: a single object
        """
        tag = Tag.query.filter_by(id=id).one_or_none()

        if not tag:
            abort(404)

        return NestedResponse(schema=TagSchema).dump(tag)

    def delete(self, id: int) -> dict:
        """Removes a selected tag.

        :param id: id of a requested tag
        :returns: whether the operation has been successful
        """
        pass

    def put(self, id: int) -> dict:
        """Modifies a selected tag.
        
        :param id: id of the tag to update
        :param payload: the data to override the tag's with
        :returns: the updated tag object
        """
        pass


class TagListAPI(Resource):
    method_decorators = [auth_required]

    def get(self) -> list:
        parser = paginated_parser.copy()
        args = parser.parse_args()
        # paginated_query = Tag.query.options(db.noload('models')).paginate(args["page"], args["per_page"], False)
        paginated_query = Tag.query.paginate(args["page"], args["per_page"], False)
        return NestedResponse(
            schema=TagSchema, 
            exclude=("models",), 
            many=True, 
            pagination=paginated_query
        ).dump(paginated_query.items)

    def post(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="No name provided")
        parser.add_argument("description", type=str)
        args = parser.parse_args()

        tag = Tag(name=args["name"], description=args["description"])
        db.session.add(tag)
        db.session.commit()

        return NestedResponse(schema=TagSchema).dump(tag)
