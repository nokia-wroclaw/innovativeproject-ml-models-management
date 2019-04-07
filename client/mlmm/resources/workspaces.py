from mlmm import BaseAction


class Workspaces(BaseAction):
    @property
    def selected(self):
        return self.config.selected_workspace

    def create(self):
        pass

    def update(self, id: int, data: dict):
        pass

    def delete(self, id: int):
        pass

    def get(self, id: int):
        pass

    def get_all(self, page=None, per_page=None):
        if not page:
            page = self.config.api_page
        if not per_page:
            per_page = self.config.api_per_page
