import json
import logging
import urllib.request

from typing import Union
from maisie import BaseAction
from maisie.utils.git import GitProvider

logger = logging.getLogger(__name__)


class Models(BaseAction):
    def upload(
        self,
        name: str,
        filename: str,
        hyperparameters: Union[str, dict],
        parameters: Union[str, dict],
        metrics: Union[str, dict],
        private: bool = False,
        dataset_name: str = "",
        dataset_description: str = "",
    ):
        hyperparameters = self._determine_input(hyperparameters)
        parameters = self._determine_input(parameters)
        metrics = self._determine_input(metrics)

        with self.config.session as session:
            files = {}
            try:
                files["file"] = open(filename, "rb")
            except FileNotFoundError:
                logger.error(f"Model `{filename}` could not be found.")

            git = GitProvider(self.config.git_local_repo)
            payload = {
                "name": name,
                "hyperparameters": json.dumps(hyperparameters),
                "parameters": json.dumps(parameters),
                "metrics": json.dumps(metrics),
                "private": private,
                "user_id": 1,
                "project_id": self.config.selected_project,
                "git_active_branch": git.active_branch,
                "git_commit_hash": git.latest_commit,
            }
            request = session.post(
                f"{self.config.api_url}/models/", files=files, data=payload
            )

            results = []
            # print(payload)
            # print(request.text)
            if "data" in request.json():
                results.append(request.json()["data"])
            else:
                logger.error("Could not upload selected model.")

            return results

    def update(self, id: int, data: dict):
        with self.config.session as session:
            pass

    def download(self, id: int):
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/models/{id}/")
            request = request.json()
            if (
                ("data") in request
                and "_links" in request["data"]
                and "download" in request["data"]["_links"]
            ):
                download_link = request["data"]["_links"]["download"]
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    (
                        "User-Agent",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
                    )
                ]
                urllib.request.install_opener(opener)
                download_data = urllib.request.urlretrieve(download_link, f"model_{id}")
                download_data = session.get(download_link)
                return download_data

    def get(self, id: int):
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/models/{id}/")
            results = []
            if "data" in request.json():
                results.append(request.json()["data"])
            else:
                logger.error("Could not fetch any models.")

        return results

    def get_all(self, page=None, per_page=None):
        results = []
        if not page:
            page = self.config.api_page
        if not per_page:
            per_page = self.config.api_per_page
        with self.config.session as session:
            request = session.get(
                f"{self.config.api_url}/models/",
                params={"page": page, "per_page": per_page},
            )
            if "data" in request.json():
                results = request.json()["data"]
                logger.debug(f"Response body: {results}")
            else:
                logger.error("Could not fetch any models.")

        return results

    def _determine_input(self, value: Union[str, dict]) -> dict:
        if isinstance(value, str):
            value = self._file_into_dict(value)

        return value

    def _file_into_dict(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as filename:
                output = json.load(filename)
        except FileNotFoundError:
            logger.error(f"JSON File `{filename}` could not be found.")
        return output
