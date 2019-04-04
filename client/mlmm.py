import cli
import configparser
import requests
import json

from utils.auth import AuthManager
from utils.git import GitProvider


class Config:
    PERMITTED_SETTINGS = [
        "api_url",
        "api_page",
        "api_per_page",
        "git_local_repo",
        "auth_user_login",
        "auth_user_password",
        "auth_app_access_token",
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
    }

    def __init__(self, filename=None, dictionary=None):
        self.fetch_from_dict(dictionary=DEFAULT_SETTINGS)
        self.fetch(filename=filename, dictionary=dictionary)
        self.__auth = None
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    @property
    def auth(self):
        if self.__auth == None:
            self.__auth = AuthManager(
                api_url=self.config.api_url,
                login=self.config.auth_user_login,
                password=self.config.auth_user_password,
                app_token=self.config.auth_app_token,
                ssh_key=self.config.auth_ssh_key,
            )
        return self.__auth

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.auth.access_token}"}

    def fetch(self, filename=None, obj=None) -> None:
        if filename:
            self.fetch_from_file(filename)
        if obj:
            self.fetch_from_dict(obj)

    def fetch_auto(self) -> None:
        # TODO: Implement traversing through user's directory tree
        pass

    def fetch_from_file(self, filename: str) -> None:
        try:
            config = configparser.ConfigParser()
            config.read(filename)
        except FileNotFoundError:
            print("FILE NOT FOUND")

    def fetch_from_dict(self, dictionary: dict) -> None:
        for key in dictionary:
            if key in PERMITTED_SETTINGS:
                setattr(self, key, dictionary[key])
            else:
                print(f"Key {key} is not allowed, skipping")


class BaseAction:
    def __init__(self, config: Config = None):
        self.config = self.__check_config(config)

    def __check_config(self, config):
        if isinstance(config, str):
            config = Config(filename=config)
        elif isinstance(config, dict):
            config = Config(dictionary=config)
        elif not isinstance(config, Config):
            config = Config()
        return config


class Projects(BaseAction):
    @property
    def selected(self):
        return self.config.project_id

    def create(self):
        pass

    def update(self, id: int, data: dict):
        pass

    def detele(self, id: int):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=self.config.api_page, per_page=self.config.api_per_page):
        pass


class Workspaces(BaseAction):
    @property
    def selected(self):
        return self.config.workspace_id

    def create(self):
        pass

    def update(self, id: int, data: dict):
        pass

    def delete(self, id: int):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=self.config.api_page, per_page=self.config.api_per_page):
        pass


class Models(BaseAction):
    @property
    def selected(self):
        pass

    def upload(self):
        pass

    def update(self, id: int, data: dict):
        pass

    def download(self, id: int):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=self.config.api_page, per_page=self.config.api_per_page):
        pass


# def upload_model(
#     name,
#     model,
#     user_id,
#     project_id,
#     dataset_name,
#     dataset_description,
#     hyperparameters,
#     parameters,
#     metrics,
#     private=False,
# ):
#     url = f"{URL}/models/"
#     git = GitProvider()
#     try:
#         files = {"file": open(model, "rb")}
#         if isinstance(hyperparameters, str):
#             with open(hyperparameters, "rb") as hp_file:
#                 hyperparameters = json.load(hp_file)
#         if isinstance(parameters, str):
#             with open(parameters, "rb") as p_file:
#                 parameters = json.load(p_file)
#         if isinstance(metrics, str):
#             with open(metrics, "rb") as m_file:
#                 metrics = json.load(m_file)

#     except FileNotFoundError:
#         print(f"Some of the requested files were not found")

#     payload = {
#         "name": name,
#         "project_id": project_id,
#         "user_id": user_id,
#         "hyperparameters": hyperparameters,
#         "parameters": parameters,
#         "metrics": metrics,
#         "dataset_name": dataset_name,
#         "dataset_description": dataset_description,
#         "git_active_branch": git.active_branch,
#         "git_commit_hash": git.latest_commit,
#         "private": private,
#     }

#     #print("PAYLOAD:", payload)
#     #auth = requests.get("https://ml.kochanowski.dev/api/v1/auth/token/", data={"login":"Nokia", "password": "Nokiademo2019"}
#     #`token = auth.body['data']['access_token']
#     r = requests.post(url, files=files, data=payload)


if __name__ == "__main__":
    cli.cli()
