from fastapi import APIRouter
from starlette.responses import HTMLResponse
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


@router.get("/{name}", response_class=HTMLResponse)
async def get_user(request: Request, name: str):
    user = await get_user_by_identifier(name)
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
