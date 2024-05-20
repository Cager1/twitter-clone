from app.http.middlewares.refresh_token_middleware import RefreshTokenMiddleware


def initialize(app):
    print("Initializing middlewares...")
    initialize_middlewares(app)
    print("Middlewares initialized.")


# register middlewares
def initialize_middlewares(app):
    app.add_middleware(RefreshTokenMiddleware)
