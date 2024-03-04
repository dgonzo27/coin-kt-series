"""Items controllers"""

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from api.models.pydantic.items import ItemPayloadSchema
from api.models.sqlalchemy import Item


def list(db: Session) -> Page[Item]:
    """Returns a list of items."""
    return paginate(db.query(Item))


def post(payload: ItemPayloadSchema, db: Session) -> Item:
    """Creates and returns a single item."""
    item = Item(**payload.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get(id: int, db: Session) -> Item:
    """Gets and returns a single item by ID."""
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item


def put(id: int, payload: ItemPayloadSchema, db: Session) -> Item:
    """Updates and returns a single item by ID."""
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
    """Deletes a single item by ID, returning a JSON response."""
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")

    db.delete(item)
    db.commit()
    return JSONResponse(
        content={"detail": f"Item ({id}) was deleted!"},
        status_code=204,
    )
