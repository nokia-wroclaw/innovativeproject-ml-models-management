import cli
import json
import requests

from utils.auth import AuthManager
from utils.git import GitProvider


class Config:
    def __init__(self):
        self.session = requests.Session()
        self.__auth = None

    @property
    def auth(self):
        if self.__auth == None:
            self.__auth = AuthManager()
        return self.__auth

    @property
    def headers(self):
        pass

    def fetch_auto(self):
        pass

    def fetch_from_file(self, filename: str):
        pass


class BaseAction:
    def __init__(self, config: Config = None):
        self.config = self.__set_config(config)

    def __set_config(self, config):
        if isinstance(config, str):
            config = Config().fetch_from_file(filename=config)
        elif not isinstance(config, Config):
            config = Config().fetch_auto()
        return config


class Projects(BaseAction):
    @property
    def selected(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def detele(self):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=1, per_page=10):
        pass


class Workspaces(BaseAction):
    @property
    def selected(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=1, per_page=10):
        pass


class Models(BaseAction):
    @property
    def selected(self):
        return self.config

    def upload(self):
        pass

    def update(self):
        pass

    def download(self):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=1, per_page=10):
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
