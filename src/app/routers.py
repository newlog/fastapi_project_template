from app.api.v1.api import api_router


def configure_routes(app):
    app.include_router(api_router)
