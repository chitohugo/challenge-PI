from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.config import configs
from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.model import User
from app.schema.base_schema import Blank
from app.schema.character_schema import Character, UpdateCharacter, PostCharacter
from app.services.character_service import CharacterService

router = APIRouter(
    prefix="/character",
    tags=["character"],
    dependencies=[Depends(JWTBearer())]
)

Page = configs.Page


@router.get("", response_model=Page[Character], dependencies=[Depends(get_current_user)])
@inject
async def get_characters(
        service: CharacterService = Depends(Provide[Container.character_service])
):
    characters = service.get_list()
    return characters


@router.get("/{id}", response_model=Character, dependencies=[Depends(get_current_user)])
@inject
async def get_character(
        id: int,
        service: CharacterService = Depends(Provide[Container.character_service])
):
    return service.get_by_id(id)


@router.post("", response_model=Character)
@inject
async def create_post(
        payload: PostCharacter,
        service: CharacterService = Depends(Provide[Container.character_service]),
        current_user: User = Depends(get_current_user)
):
    payload.user_id = current_user.id
    return service.add(payload)


@router.patch("/{id}", response_model=Character, dependencies=[Depends(get_current_user)])
@inject
async def update_character(
        id: int,
        payload: UpdateCharacter,
        service: CharacterService = Depends(Provide[Container.character_service])
):
    return service.patch(id, payload)


@router.delete("/{id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_character(
        id: int,
        service: CharacterService = Depends(Provide[Container.character_service])
):
    return service.remove_by_id(id)
