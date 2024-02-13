"""Database models"""

from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
)

from api.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default=None, nullable=False)
    price = Column(DECIMAL(11, 2), default=None, nullable=False)
    # is_offer = Column(Boolean, default=False, nullable=False)
