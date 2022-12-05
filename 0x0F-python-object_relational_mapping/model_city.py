#!/usr/bin/python3
"""A model city class"""

from sqlalchemy import ForeignKey, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Declares the citites class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
