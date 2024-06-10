from fastapi import APIRouter, Request, Response
from starlette.responses import RedirectResponse

from app.http.controllers.user_controller import *
from app.models.user import *
router = APIRouter()


@router.get("/")
async def get_users():
    return await index()


@router.get("/{user_id}")
async def get_user(user_id: int):
    return await show(user_id)

@router.get("/name/{name}")
async def get_user_by_name(name: str):
    return await get_user_by_name(name)


@router.post("/")
async def register(user: UserRegister):
    return await store(user)


@router.post("/login")
async def login_user(user: UserLogin, request: Request, response: Response):
    return await login(user, request, response)





