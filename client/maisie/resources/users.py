import json
import logging

from typing import Union
from maisie import BaseAction
from maisie.utils.git import GitProvider

logger = logging.getLogger(__name__)


class Users(BaseAction):
    def create(self, login, name, email, password):
        results = []
        with self.config.session as session:
            payload = {
                "login": login,
                "name": name,
                "email": email,
                "password": password,
            }

            request = session.post(f"{self.config.api_url}/users/", data=payload)

            if "data" in request.json():
                results.append(request.json()["data"])
            else:
                logger.error("Could not create a user.")

        return results

    def update(self, id: int, data: dict):
        pass

    def detele(self, id: int):
        pass

    def get(self, id: int):
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/users/{id}/")
            result = []
            if "data" in request.json():
                result.append(request.json()["data"])
            else:
                logger.debug(request.json())
                logger.error("Could not fetch requested user.")
        return result

    def get_all(self, page=None, per_page=None):
        results = []
        if not page:
            page = self.config.api_page
        if not per_page:
            per_page = self.config.api_per_page
        with self.config.session as session:
            request = session.get(
                f"{self.config.api_url}/users/",
                params={"page": page, "per_page": per_page},
            )
            if "data" in request.json():
                results = request.json()["data"]
                logger.debug(f"Response body: {results}")
            else:
                logger.error("Could not fetch any users.")

        return results
