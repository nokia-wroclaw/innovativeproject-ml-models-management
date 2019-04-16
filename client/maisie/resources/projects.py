import json
import logging

from typing import Union
from maisie import BaseAction
from maisie.utils.git import GitProvider

logger = logging.getLogger(__name__)


class Projects(BaseAction):
    @property
    def selected(self):
        return self.config.selected_project

    def create(self, name: str, description: str, git_url: str):
        results = []
        with self.config.session as session:
            payload = {
                "name": name,
                "description": description,
                "git_url": git_url,
                "workspace_id": self.config.selected_workspace,
            }

            request = session.post(f"{self.config.api_url}/projects/", data=payload)

            if "data" in request.json():
                results.append(request.json()["data"])
            else:
                logger.error("Could not create a project.")

        return results

    def update(self, id: int, data: dict):
        pass

    def delete(self, id: int):
        pass

    def get(self, id: int):
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/projects/{id}/")
            result = []
            if "data" in request.json():
                result.append(request.json()["data"])
            else:
                logger.error("Could not fetch requested project.")
        return result

    def get_all(self, page=None, per_page=None):
        results = []
        if not page:
            page = self.config.api_page
        if not per_page:
            per_page = self.config.api_per_page
        with self.config.session as session:
            request = session.get(
                f"{self.config.api_url}/projects/",
                params={"page": page, "per_page": per_page},
            )
            if "data" in request.json():
                results = request.json()["data"]
                logger.debug(f"Response body: {results}")
            else:
                logger.error("Could not fetch any projects.")

        return results
