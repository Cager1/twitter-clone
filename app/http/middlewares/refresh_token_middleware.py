from typing import Callable

from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from config.redis_config import r
from fastapi import APIRouter, Request, HTTPException
router = APIRouter()


class RefreshTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        session_key = request.cookies.get("session_key")
        if not session_key:
            return await call_next(request)

        # Refresh the session key in Redis here
        # This is a placeholder, replace it with your actual code
        if not r.exists(session_key):
            return await call_next(request)

        response = await call_next(request)
        # Set the refreshed session key in the response cookies
        response.set_cookie(key="session_key", value=session_key, httponly=True, max_age=3000)
        r.expire(session_key, 3000)
        return response
