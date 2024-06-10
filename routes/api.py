from fastapi import FastAPI, Request, APIRouter
from routes.model_routes import user_routes
from routes.model_routes import tweet_routes
router = APIRouter()

router.include_router(user_routes.router, tags=["users"], prefix="/users")
router.include_router(tweet_routes.router, tags=["tweets"], prefix="/tweets")

