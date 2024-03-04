"""API entrypoint"""

import logging

from fastapi import FastAPI
from fastapi_pagination import add_pagination as init_pagination

from api.config import get_settings
from api.middleware import init_middleware
from api.routes import init_routes


settings = get_settings()
logger = logging.getLogger("uvicorn")


def init_app() -> FastAPI:
    """initialize the FastAPI application"""
    _app = FastAPI(
        title=settings.api_title,
        description=settings.api_description,
        version=settings.api_version,
    )

    init_middleware(_app)
    init_pagination(_app)
    init_routes(_app)

    return _app


app = init_app()
