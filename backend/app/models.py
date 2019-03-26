from datetime import datetime

from flask import current_app, url_for
from sqlalchemy.dialects.postgresql import JSONB

from app import db, ma


users_workspaces = db.Table(
    "users_workspaces",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column(
        "workspace_id", db.Integer, db.ForeignKey("workspaces.id"), primary_key=True
    ),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(40), nullable=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=True)
    models = db.relationship("Model", backref="user", lazy=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __init__(self, **kwargs, login=None, full_name=None,
    # password=None, email=None, ):
    #     super(User, self).__init__(**kwargs)
    #     self.login = login
    #     self.full_name = full_name
    #     self.password = password
    #     self.email = email

    def __str__(self) -> str:
        return self.login

    def __repr__(self) -> str:
        return f"<User({self.id}) {self.login}>"


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "login", "full_name", "email", "models", "updated", "created")
        ordered = True


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
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=True)
    projects = db.relationship("Project", backref="workspace", lazy=True)
    users = db.relationship(
        "User",
        secondary=users_workspaces,
        lazy="subquery",
        backref=db.backref("workspaces", lazy=True),
    )
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Workspace({self.id}) {self.name}>"

    def __str__(self) -> str:
        return self.name


class WorkspaceSchema(ma.Schema):
    class Meta:
        model = Workspace
        fields = (
            "id",
            "name",
            "description",
            "projects",
            "users",
            "updated",
            "created",
        )
        ordered = True


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=True)
    workspace_id = db.Column(db.Integer, db.ForeignKey("workspaces.id"), nullable=False)
    models = db.relationship("Model", backref="project", lazy=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Project({self.id}) {self.name}>"


class ProjectSchema(ma.Schema):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "workspace_id",
            "models",
            "updated",
            "created",
        )
        ordered = True


# class SessionToken(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"<SessionToken({self.id}) {self.name}>"


class Model(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
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
        return self.name

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
