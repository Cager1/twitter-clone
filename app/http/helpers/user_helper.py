from redis.commands.helpers import random_string

from database.connection import db
from database.models.user import User
from config.redis_config import r


async def get_user_by_session(session_key: str):
    print(f"Session key: {session_key}")
    if session_key is None:
        return None
    email = r.get(session_key)
    if email:
        user = db.query(User).filter(User.email == email).first()
        return user
    return None


async def generate_session_key(user):
    # generate session key, random string
    session_key = random_string(96)
    try:
        r.set(session_key, user.email, ex=3000)
    except Exception as e:
        print(f"Error setting key in Redis: {e}")
    return session_key
