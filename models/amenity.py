#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class Amenity(BaseModel, Base):
    """
    Amenity class inherits from BaseModel and Base
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
