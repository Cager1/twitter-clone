from fastapi import HTTPException, Request, Response
from passlib.hash import bcrypt
from redis.commands.helpers import random_string
from config.redis_config import r
from database.models.user import User
from app.http.resources.user_resource import UserResource
from database.connection import db



# get all users
async def index():
    users = db.query(User).all()
    return UserResource(users)


async def show(user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return UserResource(user)


# create user
async def store(user):
    if user.password != user.password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User with that email already exists")

    user.identifier = await create_identifier(user.name)

    hashed_password = bcrypt.hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        identifier=user.identifier
    )
    db.add(db_user)
    db.commit()
    return {"message": "User created"}


# function to create identifier
async def create_identifier(name: str):
    identifier  = name.lower().replace(" ", "-")
    # check if user with that identifier already exists and if it exists add number to the end and increment it until it is unique
    user = db.query(User).filter(User.identifier == identifier).first()
    if user:
        i = 1
        while db.query(User).filter(User.identifier == f"{identifier}-{i}").first():
            i += 1
        identifier = f"{identifier}-{i}"
    return identifier


async def update(user_id: int, user):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()

    return UserResource(db_user)


async def get_user_by_identifier(identifier: str):
    user = db.query(User).filter(User.identifier == identifier).first()
    return UserResource(user)


async def generate_session_key(user):
    # generate session key, random string
    session_key = random_string(96)
    try:
        r.set(session_key, user.email, ex=3000)
    except Exception as e:
        print(f"Error setting key in Redis: {e}")
    return session_key


async def login(user, request: Request, response: Response):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        if bcrypt.verify(user.password, db_user.hashed_password):
            session_key = await generate_session_key(db_user)
            response.set_cookie(key="session_key", value=session_key, httponly=True, max_age=3000)
            return {"message": "Login successful"}
        else:
            return {"message": "Login failed"}
    else:
        return {"message": "Login failed"}
