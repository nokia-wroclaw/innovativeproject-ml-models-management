from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_uploads import UploadSet, configure_uploads, ALL
from flask_praetorian import Praetorian
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
praetorian = Praetorian()
cors = CORS()

models_uploadset = UploadSet(name="models", extensions=ALL)


def create_app(config_object: str = "Production") -> object:
    """Creates Flask app using one of provided configuration objects.
    
    :param config_object: a configuration object defined in config.py
    :returns: a created app 
    """
    app = Flask(__name__)
    app.config.from_object(f"app.config.{config_object}Config")

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)
    configure_uploads(app, (models_uploadset,))

    from app.models import User

    praetorian.init_app(app, User)

    from app.api import api_bp
    from app.storage import storage_bp

    app.register_blueprint(api_bp, url_prefix="/api/v1")
    app.register_blueprint(storage_bp, url_prefix="/storage")

    return app


from app import models
