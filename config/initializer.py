from config.routes import initialize as initialize_routes
from config.middlewares import initialize as initialize_middlewares


def initialize(app):
    initialize_routes(app)
    initialize_middlewares(app)

