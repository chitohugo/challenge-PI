from fastapi import APIRouter

from interface.endpoints.auth import router as auth_router
from interface.endpoints.character import router as character_router
from interface.endpoints.user import router as user_router

routers = APIRouter()
router_list = [auth_router, user_router, character_router]

[routers.include_router(router) for router in router_list]
