from fastapi import FastAPI, Request, APIRouter
from routes.model_routes import user_routes
from starlette.templating import Jinja2Templates
router = APIRouter()

router.include_router(user_routes.router, tags=["users"], prefix="/users")
