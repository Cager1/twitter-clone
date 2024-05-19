from fastapi import HTTPException
from passlib.hash import bcrypt
from database.models.user import User
from app.http.resources.user_resource import UserResource
from database.connection import db


# function to follow a user
async def follow(follower_id: int, following_id: int):
    follower = db.query(User).filter(User.id == follower_id).first()
    following = db.query(User).filter(User.id == following_id).first()
    if not follower or not following:
        raise HTTPException(status_code=404, detail="User not found")
    follower.following.append(following)
    db.commit()
    return {"message": "User followed"}
