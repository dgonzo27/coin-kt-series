"""Items views"""

from fastapi import APIRouter, Depends, Path, Response
from fastapi_pagination import Page
from sqlalchemy.orm import Session

from api.controllers import items
from api.db import get_db
from api.models.pydantic import items as models


router = APIRouter()


@router.get("", response_model=Page[models.ItemResponseSchema], status_code=200)
def list_items(db: Session = Depends(get_db)) -> Response:
    return items.list(db)


@router.get("/{id}", response_model=models.ItemResponseSchema, status_code=200)
def get_item(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
) -> Response:
    return items.get(id, db)


@router.post("", response_model=models.ItemResponseSchema, status_code=201)
def create_item(
    payload: models.ItemPayloadSchema,
    db: Session = Depends(get_db),
) -> Response:
    return items.post(payload, db)


@router.put("/{id}", response_model=models.ItemResponseSchema, status_code=200)
def update_item(
    payload: models.ItemPayloadSchema,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
) -> Response:
    return items.put(id, payload, db)


@router.delete("/{id}", status_code=204)
def delete_item(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
) -> Response:
    return items.delete(id, db)
