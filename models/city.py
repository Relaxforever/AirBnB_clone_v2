#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import String, Column, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state = relationship('State', cascade='delete', backref='City')
