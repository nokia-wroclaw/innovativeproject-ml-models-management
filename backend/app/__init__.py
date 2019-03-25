from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

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

    from app.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    return app


from app import models
