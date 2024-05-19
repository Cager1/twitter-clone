from fastapi import APIRouter
from routes.model_view_routes import user_routes

router = APIRouter()
router.include_router(user_routes.router, tags=["users"])


# @router.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     # You can pass dynamic data to the template here
#     return templates.TemplateResponse("index.html",
#                                       {
#                                           "request": request,
#                                           "title": "Hello, FastAPI!",
#                                           "content": "This is a simple example of using HTML templates with FastAPI."
#                                       })
#
# @router.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
