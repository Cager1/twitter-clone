from fastapi import APIRouter
from app.http.controllers.follower_controller import *
from app.models.follower import *
router = APIRouter()

# follow a user
@router.post("/follow")
async def follow_user(follower: Follower):
    return await follow(follower.follower_id, follower.following_id)

