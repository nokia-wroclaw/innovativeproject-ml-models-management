import os
from flask import Blueprint, current_app, abort, send_file
from flask_restful import Resource, Api, reqparse

from app import models_uploadset
from app.models import Model


class StorageDownloadAPI(Resource):
    def get(self, id):
        model = Model.query.filter_by(id=id).first()

        if not model:
            abort(404)

        return send_file(
            os.path.join(models_uploadset.path(model.path)), as_attachment=True
        )


storage_bp = Blueprint("storage", __name__)
storage = Api(storage_bp)

storage.add_resource(
    StorageDownloadAPI, "/download/<int:id>/", endpoint="download_model"
)
