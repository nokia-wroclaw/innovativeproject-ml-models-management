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
        """Creates and posts a new project

        :param name: name of a project to create
        :param desription: description of a project to create
        :param git_url: path to git repository with the project

        :returns: created project
        """
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
        """Updates selected project.
        :param id: id of project to update
        :param data: dictionary

        :returns: updated project
        """
        pass

    def delete(self, id: int):
        """Deletes selected project.
        :param id: id of the project to delete
        
        :returns: deleted project
        """
        pass

    def get(self, id: int):
        """Fetches a single project

        :param id: id of the project to get
        :returns: requested project
        """
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/projects/{id}/")
            result = []
            if "data" in request.json():
                result.append(request.json()["data"])
            else:
                logger.error("Could not fetch requested project.")
        return result

    def get_all(self, query=None, page=None, per_page=None):
        """Fetches all projects that satisfy some condition.
        
        :param query: query string
        :param page: number of the page used in pagination
        :param per_page: number of the items to be fetched
        :returns: a list of returned projects
        """
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
