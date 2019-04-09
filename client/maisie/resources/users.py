from maisie import BaseAction


class Users(BaseAction):
    def create(self):
        pass

    def update(self, id: int, data: dict):
        pass

    def detele(self, id: int):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=None, per_page=None):
        if not page:
            page = self.config.api_page
        if not per_page:
            per_page = self.config.api_per_page
