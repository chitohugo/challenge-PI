from dependency_injector import containers, providers

from infrastructure.config import configs
from data.database import Database
from data.repository.character_repository import CharacterRepository
from data.repository.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.services.character_service import CharacterService
from app.services.user_service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface.endpoints.auth",
            "interface.endpoints.user",
            "interface.endpoints.character",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    character_repository = providers.Factory(CharacterRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    character_service = providers.Factory(CharacterService, character_repository=character_repository)
