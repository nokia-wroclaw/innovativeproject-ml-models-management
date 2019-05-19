import json
import logging

from typing import Union
from maisie import BaseAction
from maisie.utils.git import GitProvider

logger = logging.getLogger(__name__)


class Users(BaseAction):
    def create(self, login, name, email, password):
        """Creates and posts a new user

        :param login: login of a user to create
        :param name: name of a user to create
        :param email: email of user to create
        :param password: password of user to create

        :returns: created user
        """
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
        """Updates selected user.
        :param id: id of user to update
        :param data: dictionary

        :returns: updated user
        """
        pass

    def detele(self, id: int):
        """Deletes selected user.
        :param id: id of the user to delete
        
        :returns: deleted user
        """
        pass

    def get(self, id: int):
        """Fetches a single user

        :param id: id of the user to get
        :returns: requested user
        """
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/users/{id}/")
            result = []
            if "data" in request.json():
                result.append(request.json()["data"])
            else:
                logger.debug(request.json())
                logger.error("Could not fetch requested user.")
        return result

    def get_all(self, query=None, page=None, per_page=None):
        """Fetches all users that satisfy some condition.
        
        :param query: query string
        :param page: number of the page used in pagination
        :param per_page: number of the items to be fetched
        :returns: a list of returned users
        """
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
