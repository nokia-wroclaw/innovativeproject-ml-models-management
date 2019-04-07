import logging
from mlmm import BaseAction

logger = logging.getLogger(__name__)


class Models(BaseAction):
    def upload(self):
        with self.config.session as session:
            files = []
            payload = {}
            session.post(f"{self.config.api_url}/models/", files=files, data=payload)

    def update(self, id: int, data: dict):
        with self.config.session as session:
            pass

    def download(self, id: int):
        with self.config.session as session:
            pass

    def get(self, id: int):
        with self.config.session as session:
            request = session.get(f"{self.config.api_url}/models/{id}/")
            logger.debug(f"Response data: {request.json()}")

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
            results = request.json()["data"]
            logger.debug(f"Response body: {results}")

        return results
