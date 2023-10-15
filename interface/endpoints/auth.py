from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from infrastructure.container import Container
from interface.schema.auth_schema import SignIn, SignInResponse, SignUp
from interface.schema.user_schema import User
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/sign-in", response_model=SignInResponse)
@inject
async def sign_in(payload: SignIn, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_in(payload)


@router.post("/sign-up", response_model=User)
@inject
async def sign_up(payload: SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_up(payload)
