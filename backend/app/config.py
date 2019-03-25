import os


class Config(object):
    """Shared configuration for all environments."""

    DEBUG = False
    TESTING = False
    # Display errors for every field in Flask-RESTful on request parsing
    # https://flask-restful.readthedocs.io/en/latest/reqparse.html#error-handling
    BUNDLE_ERRORS = True

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "super-secret-key"
    db_user = os.environ.get("POSTGRES_USER")
    db_pass = os.environ.get("POSTGRES_PASSWORD")
    db_name = os.environ.get("POSTGRES_DB")
    db_host = os.environ.get("POSTGRES_HOST") or "postgresdb"
    db_port = os.environ.get("POSTGRES_PORT") or 5432

    DATABASE_URI = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_DEFAULT_ENTRIES_PER_PAGE = os.environ.get("API_DEFAULT_ENTRIES_PER_PAGE")
    API_MAX_ENTRIES_PER_PAGE = os.environ.get("API_MAX_ENTRIES_PER_PAGE")


class ProductionConfig(Config):
    """Object used to configure the app on production."""

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


class DevelopmentConfig(Config):
    """Object used to configure the app for local development."""

    DEBUG = True


class TestingConfig(Config):
    """Object used to configure the app for testing environments."""

    TESTING = True
