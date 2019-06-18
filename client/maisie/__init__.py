import coloredlogs
import yaml
import logging
import logging.config
import pkg_resources
import os

resource_package = __name__
resource_path = "/".join(("logging.yaml",))
template = pkg_resources.resource_stream(resource_package, resource_path)

with pkg_resources.resource_stream(resource_package, resource_path) as stream:
    logging_config = yaml.load(stream, Loader=yaml.SafeLoader)

logging.config.dictConfig(logging_config)

LOGGING_LEVEL = os.environ.get("MAISIE_LOGGING_LEVEL") or "ERROR"
coloredlogs.install(
    fmt=logging_config["formatters"]["simple"]["format"], level=LOGGING_LEVEL
)

PERMITTED_SETTINGS = [
    "api_url",
    "api_page",
    "api_per_page",
    "git_local_repo",
    "auth_user_login",
    "auth_user_password",
    "auth_app_token",
    "auth_ssh_key",
    "logging_enable",
    "logging_level",
    "logging_file",
    "selected_project",
    "selected_workspace",
]

DEFAULT_SETTINGS = {
    "api_page": 1,
    "api_per_page": 10,
    "logging_enable": True,
    "logging_level": "INFO",
    "logging_file": None,
    "auth_user_password": None,
    "auth_app_token": None,
    "auth_ssh_key": None,
}

APP_ENV_PREFIX = "MAISIE"

from maisie.core import Config, BaseAction
from maisie.resources.models import Models
from maisie.resources.projects import Projects
from maisie.resources.workspaces import Workspaces
from maisie.resources.users import Users
