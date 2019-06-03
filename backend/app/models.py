from datetime import datetime

import sqlalchemy
from flask import current_app, url_for
from sqlalchemy.dialects.postgresql import JSONB

from app import db, ma, praetorian

users_workspaces = db.Table(
    "users_workspaces",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column(
        "workspace_id", db.Integer, db.ForeignKey("workspaces.id"), primary_key=True
    ),
)

tags_association_table = db.Table(
    "association",
    db.metadata,
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")),
    db.Column("model_id", db.Integer, db.ForeignKey("models.id")),
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

    def __init__(self, login, password, full_name=None, email=None):
        self.login = login
        self.password = praetorian.encrypt_password(password)
        self.full_name = full_name
        self.email = email

    @property
    def rolenames(self):
        roles = "admin,test"
        try:
            return roles.split(",")
        except Exception:
            return []

    @classmethod
    def lookup(cls, login):
        return cls.query.filter_by(login=login).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def __str__(self) -> str:
        return self.login

    def __repr__(self) -> str:
        return f"<User({self.id}) {self.login}>"


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "login", "full_name", "email", "updated", "created")
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
        fields = ("id", "name", "description", "updated", "created")
        ordered = True


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    description = db.Column(db.Text, nullable=True)
    models = db.relationship(
        "Model",
        secondary=tags_association_table,
        lazy="subquery",
        backref=db.backref("tags", lazy=True),
    )

    def __repr__(self) -> str:
        return f"<Tag({self.id}) {self.name}>"

    def __str__(self) -> str:
        return self.name


class TagSchema(ma.Schema):
    class Meta:
        model = Tag
        fields = ("id", "description", "models")
        ordered = True


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=True)
    workspace_id = db.Column(db.Integer, db.ForeignKey("workspaces.id"), nullable=False)
    models = db.relationship("Model", backref="project", lazy=True)
    git_url = db.Column(db.String, nullable=True)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Project({self.id}) {self.name}>"


class ProjectSchema(ma.Schema):
    # models = ma.Nested('ModelSchema', many=True)
    class Meta:
        model = Project
        fields = (
            "id",
            "workspace_id",
            "name",
            "description",
            "all_hyperparameters",
            "all_parameters",
            "all_metrics",
            "all_users",
            "git_url",
            "updated",
            "created",
            "_links",
        )
        ordered = True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("api.project", id="<id>", _external=True),
            "workspace": ma.URLFor(
                "api.workspace", id="<workspace_id>", _external=True
            ),
        }
    )

    all_hyperparameters = ma.Method("get_all_hyperparameters")
    all_parameters = ma.Method("get_all_parameters")
    all_metrics = ma.Method("get_all_metrics")
    all_users = ma.Method("get_all_users")

    def get_all_hyperparameters(self, obj):
        query = f"SELECT jsonb_object_keys(hyperparameters) from models WHERE project_id = {obj.id};"
        keys = db.engine.execute(query)
        output = []
        for key in keys:
            output.append(key[0])
        return output

    def get_all_parameters(self, obj):
        query = f"SELECT jsonb_object_keys(parameters) from models WHERE project_id = {obj.id};"
        keys = db.engine.execute(query)
        output = []
        for key in keys:
            output.append(key[0])
        return output

    def get_all_metrics(self, obj):
        query = f"SELECT jsonb_object_keys(metrics) from models WHERE project_id = {obj.id};"
        keys = db.engine.execute(query)
        output = []
        for key in keys:
            output.append(key[0])
        return output

    def get_all_users(self, obj):
        models = Model.query.filter_by(project_id=obj.id).distinct(Model.user_id)
        output = []
        for model in models:
            output.append({"id": model.user.id, "full_name": model.user.full_name})

        return output


class Model(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    hyperparameters = db.Column(JSONB)
    parameters = db.Column(JSONB)
    metrics = db.Column(JSONB)
    name = db.Column(db.String(40), default=None)
    path = db.Column(db.Text, default=None)
    dataset_name = db.Column(db.String(120), default=None)
    dataset_description = db.Column(db.Text, default=None)
    git_active_branch = db.Column(db.String, nullable=True)
    git_commit_hash = db.Column(db.String, nullable=True)
    private = db.Column(db.Boolean, default=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        db.Index("ix_model_hyperparameters", hyperparameters, postgresql_using="gin"),
        db.Index("ix_model_parameters", parameters, postgresql_using="gin"),
        db.Index("ix_model_metrics", metrics, postgresql_using="gin"),
    )

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
            "user",
            "project_id",
            "name",
            "visibility",
            "dataset",
            "hyperparameters",
            "parameters",
            "metrics",
            "tags",
            "git",
            "created",
            "updated",
            "_links",
        )
        ordered = True

    visibility = ma.Function(lambda obj: "private" if obj.private else "public")
    dataset = ma.Method("get_dataset_details")
    git = ma.Method("get_version_control_details")
    user = ma.Nested(UserSchema(exclude=("created", "updated", "email")))
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("api.model", id="<id>", _external=True),
            "user": ma.URLFor("api.user", id="<user_id>", _external=True),
            "project": ma.URLFor("api.project", id="<project_id>", _external=True),
            "download": ma.URLFor("storage.download_model", id="<id>", _external=True),
        }
    )

    def get_dataset_details(self, obj):
        return {"name": obj.dataset_name, "description": obj.dataset_description}

    def get_version_control_details(self, obj):
        return {
            "active_branch": obj.git_active_branch,
            "commit_hash": obj.git_commit_hash,
        }
