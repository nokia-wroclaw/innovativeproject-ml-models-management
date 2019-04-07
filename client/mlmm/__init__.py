import coloredlogs
import yaml
import logging
import logging.config

with open("logging.yaml", "r") as stream:
    logging_config = yaml.load(stream, Loader=yaml.SafeLoader)

logging.config.dictConfig(logging_config)

coloredlogs.install(fmt=logging_config["formatters"]["simple"]["format"], level="ERROR")

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

APP_ENV_PREFIX = "MLMM"

from mlmm.core import Config, BaseAction
from mlmm.resources.models import Models
from mlmm.resources.projects import Projects
from mlmm.resources.workspaces import Workspaces
from mlmm.resources.users import Users