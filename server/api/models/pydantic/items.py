"""Items pydantic models"""

from typing import Optional

from pydantic import BaseModel


class ItemPayloadSchema(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = False


class ItemResponseSchema(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool
