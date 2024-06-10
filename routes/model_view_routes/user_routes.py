from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from app.http.dependencies.auth_dependency import verify_session_key
from app.http.views.homepage import return_homepage
from config.templates import templates
from app.http.controllers.user_controller import *
from app.models.user import *
from starlette.requests import Request

router = APIRouter()


@router.get("/{identifier}", response_class=HTMLResponse)
async def get_user(request: Request, identifier: str):
    user = await get_user_by_identifier(identifier)
    return templates.TemplateResponse("user/show.html",
                                      {
                                          "request": request,
                                          "user": user.user
                                      })
