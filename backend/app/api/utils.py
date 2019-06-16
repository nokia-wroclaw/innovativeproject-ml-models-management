class NestedResponse:
    def __init__(self, schema=None, many=False, pagination=None):
        self.schema = schema
        self.many = many
        self.pagination = pagination

    def gather_pagination_info(self):
        pagination = self.pagination

        return {
            "has_next": self.pagination.has_next,
            "has_prev": self.pagination.has_prev,
            "page": self.pagination.page,
            "per_page": self.pagination.per_page,
            "total_pages": self.pagination.pages,
            "total_items": self.pagination.total,
        }

    def dump(self, data):
        response = {}
        if self.schema != None:
            data = self.schema(many=self.many).dump(data)
        response["data"] = data
        if self.pagination != None:
            response["pagination"] = self.gather_pagination_info()

        return response
