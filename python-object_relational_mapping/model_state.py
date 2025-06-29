#!/usr/bin/python3
"""
Module that defines the State class mapped to the 'states' table
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class mapped to the 'states' table.

    Attributes:
        id (int): Primary key, auto-incremented, not nullable.
        name (str): Name of the state, max length 128 characters, not nullable.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
