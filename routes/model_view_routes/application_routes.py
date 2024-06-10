from fastapi import APIRouter, Depends, Query, Form
from starlette.responses import HTMLResponse

from app.http.controllers.user_controller import store
from app.http.views.homepage import *
from starlette.requests import Request

from app.models.user import UserRegister
from config.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return await return_homepage(request)


@router.get("/auth/logout")
async def logout(request: Request):
    return await return_logout(request)


@router.post("/auth/register", response_class=HTMLResponse)
async def register(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    user = UserRegister(name=name, email=email, password=password, password_confirmation=confirm_password)
    await store(user)
    return RedirectResponse(url="/auth/login", status_code=303)

@router.get("/auth/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("auth/login.html",
                                      {
                                          "request": request
                                      })


@router.get("/auth/register", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("auth/register.html",
                                      {
                                          "request": request
                                      })
