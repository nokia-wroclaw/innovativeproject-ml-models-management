from datetime import datetime

from flask import current_app, url_for
from sqlalchemy.dialects.postgresql import JSONB

from app import db, ma


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<User({self.id}) {self.name}>"


# class ConnectedApp(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __str(self) -> str:
#         return self.name

#     def __repr__(self) -> str:
#         return f"<ConnectedApp({self.id}) {self.name}>"


class Workspace(db.Model):
    __tablename__ = "workspaces"

    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Workspace({self.id}) {self.name}>"

    def __str__(self) -> str:
        return self.name


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Project({self.id}) {self.name}>"


# class SessionToken(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"<SessionToken({self.id}) {self.name}>"


class Model(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True)
    hyperparameters = db.Column(JSONB)
    parameters = db.Column(JSONB)
    name = db.Column(db.String(40), default=None)
    path = db.Column(db.Text, default=None)
    dataset_name = db.Column(db.String(120), default=None)
    dataset_description = db.Column(db.Text, default=None)
    private = db.Column(db.Boolean, default=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        db.Index("ix_model_hyperparameters", hyperparameters, postgresql_using="gin"),
        db.Index("ix_model_parameters", parameters, postgresql_using="gin"),
    )

    def __init__(self) -> object:
        pass

    def __str__(self) -> str:
        return self.model_name

    def __repr__(self) -> str:
        return "".join(
            [
                f"<Model {self.name}, hyperparams={self.hyperparameters}, ",
                f"params={self.parameters}, private={self.private}>",
            ]
        )


class ModelSchema(ma.Schema):
    class Meta:
        model = Model
        fields = (
            "id",
            "name",
            "path",
            "visibility",
            "dataset",
            "hyperparameters",
            "parameters",
            "created",
            "updated",
            "_links",
        )
        ordered = True

    visibility = ma.Function(lambda obj: "private" if obj.private else "public")
    dataset = ma.Method("get_dataset_information")
    _links = ma.Hyperlinks({"self": ma.URLFor("api.model", id="<id>", _external=True)})

    def get_dataset_information(self, obj):
        return {"name": obj.dataset_name, "description": obj.dataset_description}
