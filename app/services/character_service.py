from app.repository.character_repository import CharacterRepository
from app.services.base_service import BaseService


class CharacterService(BaseService):
    def __init__(self, character_repository: CharacterRepository):
        self.character_repository = character_repository
        super().__init__(character_repository)
