"""API middleware"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def init_middleware(app: FastAPI) -> None:
    """initialize application middleware"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
