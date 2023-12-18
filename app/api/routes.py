from fastapi import APIRouter

from interface.endpoints import *

routers = APIRouter()
router_list = [auth_router, user_router, character_router]

[routers.include_router(router) for router in router_list]
