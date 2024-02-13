"""Items controllers"""

from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import desc
from sqlalchemy.orm import Session

from api.models.pydantic.items import ItemPayloadSchema
from api.models.sqlalchemy import Item


def list(db: Session) -> List[Item]:
    """list all items"""
    return db.query(Item).all()


def get(id: int, db: Session) -> Item:
    """get a single item"""
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item


def post(payload: ItemPayloadSchema, db: Session) -> Item:
    """create a single item"""
    item = Item(**payload.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def put(id: int, payload: ItemPayloadSchema, db: Session) -> Item:
    """update a single item"""
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")

    obj_data = jsonable_encoder(item)
    put_data = payload.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in put_data:
            setattr(item, field, put_data[field])
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete(id: int, db: Session) -> JSONResponse:
    """delete a single item"""
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")

    db.delete(item)
    db.commit()
    return JSONResponse(
        content={"detail": f"Item ({id}) was deleted!"},
        status_code=204,
    )
