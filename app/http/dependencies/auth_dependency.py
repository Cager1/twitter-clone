from fastapi import Depends, HTTPException, Request
from database.connection import db
from database.models.user import User
from config.redis_config import r
from typing import Optional


def verify_session_key(request: Request):
    session_key = request.cookies.get("session_key")
    if not session_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

    email = r.get(session_key)
    if not email:
        raise HTTPException(status_code=401, detail="Unauthorized")
    # get user with email
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user
