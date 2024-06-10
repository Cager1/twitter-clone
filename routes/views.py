from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from app.http.views.homepage import return_homepage
from config.templates import templates
from routes.model_view_routes import user_routes
from routes.model_view_routes import application_routes

router = APIRouter()
router.include_router(user_routes.router, tags=["users"])
router.include_router(application_routes.router, tags=["application"])

