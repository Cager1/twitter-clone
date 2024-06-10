from fastapi import APIRouter, Request, Response, Depends

from app.http.dependencies.auth_dependency import verify_session_key
from app.http.helpers.user_helper import get_user_by_session
from app.http.controllers.tweet_controller import *
from app.models.tweet import *

router = APIRouter()


@router.get("/")
async def get_tweets():
    return await index()


@router.post("/")
async def create_tweet(request: Request, response: Response, tweet: TweetStore, user: str = Depends(verify_session_key)):
    return await store(tweet, user)
