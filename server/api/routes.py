"""API routes"""

from fastapi import FastAPI

from api.views.items import router as item_router


def init_routes(app: FastAPI) -> None:
    """initialize application routes"""
    app.include_router(
        router=item_router,
        prefix="/items",
        tags=["Items"],
    )
