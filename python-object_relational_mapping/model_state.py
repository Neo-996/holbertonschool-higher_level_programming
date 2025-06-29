#!/usr/bin/python3
"""
Defines the State class mapped to the 'states' table in MySQL database
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative class definitions
Base = declarative_base()

class State(Base):
    """
    State class mapped to the 'states' table.

    Attributes:
        id (int): Primary key, auto-incremented, non-nullable.
        name (str): State name, max length 128 characters, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
