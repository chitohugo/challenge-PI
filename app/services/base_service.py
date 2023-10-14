class BaseService:
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_list(self):
        return self._repository.read()

    def get_by_id(self, id: int):
        return self._repository.read_by_id(id)

    def add(self, schema):
        return self._repository.create(schema)

    def patch(self, id: int, schema):
        return self._repository.update(id, schema)

    def remove_by_id(self, id):
        return self._repository.delete_by_id(id)
