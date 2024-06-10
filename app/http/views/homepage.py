from starlette.responses import RedirectResponse, Response

from app.http.controllers.user_controller import get_suggested_users
from app.http.helpers.user_helper import get_user_by_session
from app.http.controllers.tweet_controller import index as get_tweets
from config.templates import templates
from fastapi import Request
from app.http.controllers.user_controller import logout


async def return_homepage(request: Request):
    #from request cookie get session key and find user
    session_key = request.cookies.get("session_key")
    user = await get_user_by_session(session_key)
    tweets = await get_tweets()
    suggested_users = await get_suggested_users()
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "user": user,
                                          "tweets": tweets,
                                          "suggested_users": suggested_users
                                      })


async def return_logout(request: Request):
    response = Response()
    await logout(request, response)
    return RedirectResponse(url="/", status_code=303)
