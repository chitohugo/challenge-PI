from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.config import configs
from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.character_schema import UpdateCharacter
from app.schema.user_schema import User
from app.services.user_service import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(JWTBearer())]
)

Page = configs.Page


@router.get("", response_model=Page[User], dependencies=[Depends(get_current_user)])
@inject
async def get_users(
        service: UserService = Depends(Provide[Container.user_service])
):
    users = service.get_list()
    return users


@router.get("/{id}", response_model=User, dependencies=[Depends(get_current_user)])
@inject
async def get_user(
        id: int,
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_by_id(id)


@router.patch("/{id}", response_model=User, dependencies=[Depends(get_current_user)])
@inject
async def update_user(
        id: int,
        user: UpdateCharacter,
        service: UserService = Depends(Provide[Container.user_service])
):
    return service.patch(id, user)


@router.delete("/{id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_user(
        id: int,
        service: UserService = Depends(Provide[Container.user_service])
):
    return service.remove_by_id(id)
