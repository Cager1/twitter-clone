from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from app.http.dependencies.auth_dependency import verify_session_key
from config.templates import templates
from app.http.controllers.user_controller import *
from app.models.user import *
from starlette.requests import Request

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    print("Request: ", request)
    # You can pass dynamic data to the template here
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "title": "Hello, FastAPI!",
                                          "content": "This is a simple example of using HTML templates with FastAPI."
                                      })


@router.get("/{identifier}", response_class=HTMLResponse)
async def get_user(request: Request, identifier: str, email: str = Depends(verify_session_key)):
    user = await get_user_by_identifier(identifier)
    return templates.TemplateResponse("user/show.html",
                                      {
                                          "request": request,
                                          "user": user.user
                                      })


@router.get("/auth/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("auth/login.html",
                                      {
                                          "request": request
                                      })
