import os


class Config(object):
    """Shared configuration for all environments."""

    DEBUG = False
    TESTING = False
    # Display errors for every field in Flask-RESTful on request parsing
    # https://flask-restful.readthedocs.io/en/latest/reqparse.html#error-handling
    BUNDLE_ERRORS = True

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "super-secret-key")
    db_user = os.environ.get("POSTGRES_USER")
    db_pass = os.environ.get("POSTGRES_PASSWORD")
    db_name = os.environ.get("POSTGRES_DB")
    db_host = os.environ.get("POSTGRES_HOST", "postgresdb")
    db_port = os.environ.get("POSTGRES_PORT", 5432)

    DATABASE_URI = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADS_DEFAULT_DEST = (
        os.environ.get("MODELS_TMP_STORAGE_DIRECTORY", "/var/maisie/uploads") 
    )
    UPLOADS_DEFAULT_URL = (
        os.environ.get("MODELS_DEFAULT_DOWNLOAD_URL", "https://localhost:5000")
    )


class ProductionConfig(Config):
    """Object used to configure the app on production."""

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


class DevelopmentConfig(Config):
    """Object used to configure the app for local development."""

    JWT_ACCESS_LIFESPAN = {"minutes": 45}
    DEBUG = True


class TestingConfig(Config):
    """Object used to configure the app for testing environments."""

    TESTING = True
