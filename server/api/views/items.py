"""Items views"""

from typing import List

from fastapi import APIRouter, Depends, Path, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.db import get_db
from api.models.pydantic import items as models


router = APIRouter()


@router.get("", response_model=List[models.ItemResponseSchema], status_code=200)
def list_items() -> Response:
    return [
        {
            "id": 1,
            "name": "Cookies",
            "price": 2.34,
            "is_offer": False,
        }
    ]


@router.get("/{id}", response_model=models.ItemResponseSchema, status_code=200)
def get_item(id: int = Path(..., gt=0)) -> Response:
    return {
        "id": id,
        "name": "Cookies",
        "price": 2.34,
        "is_offer": False,
    }


@router.post("", response_model=models.ItemResponseSchema, status_code=201)
def create_item(payload: models.ItemPayloadSchema) -> Response:
    return {
        "id": 1,
        "name": payload.name,
        "price": payload.price,
        "is_offer": payload.is_offer,
    }


@router.put("/{id}", response_model=models.ItemResponseSchema, status_code=200)
def update_item(
    payload: models.ItemPayloadSchema, id: int = Path(..., gt=0)
) -> Response:
    return {
        "id": id,
        "name": payload.name,
        "price": payload.price,
        "is_offer": payload.is_offer,
    }


@router.delete("/{id}", status_code=204)
def delete_item(id: int = Path(..., gt=0)) -> Response:
    return JSONResponse(
        content={"detail": f"Item ({id}) was deleted!"},
        status_code=204,
    )
