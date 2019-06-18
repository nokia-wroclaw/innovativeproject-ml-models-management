from flask import jsonify, request, abort
from flask_restful import Resource, reqparse

from app import db
from app.models import Tag, Model, ModelSchema, Workspace
from app.api import paginated_parser
from app.api.utils import NestedResponse

from app.api import current_app


class ModelTagAssocAPI(Resource):
    def post(self, model_id: int, tag_id: int) -> dict:
        model = Model.query.filter_by(id=model_id).first()
        tag = Tag.query.filter_by(id=tag_id).first()
        if not (model and tag):
            abort(404)
        tag.models.append(model)
        current_app.logger.info(
            "tag " + str(tag_id) + " added to model " + str(model_id)
        )
        db.session.add(tag)
        db.session.commit()
        return NestedResponse(schema=ModelSchema).dump(model)

    def delete(self, model_id: int, tag_id: int) -> dict:
        model = Model.query.filter_by(id=model_id).first()
        tag = Tag.query.filter_by(id=tag_id).first()
        if not (model and tag):
            abort(404)
        tag.models.remove(model)
        current_app.logger.info(
            "tag " + str(tag_id) + " dropped from model " + str(model_id)
        )
        db.session.add(tag)
        db.session.commit()
        return NestedResponse(schema=ModelSchema).dump(model)
