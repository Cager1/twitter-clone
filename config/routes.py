from routes.views import router as views_router
from routes.api import router as api_router

def initialize(app):
    print("Initializing routes...")
    initialize_routes(app)
    print("Routes initialized.")


def initialize_routes(app):
    app.include_router(views_router, prefix="")
    app.include_router(api_router, prefix="/api")
