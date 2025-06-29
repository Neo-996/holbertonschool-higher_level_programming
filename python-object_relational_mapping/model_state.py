#!/usr/bin/python3
"""
This module defines the State class mapped to the states table
using SQLAlchemy ORM. It also creates the Base instance for
declarative mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base instance for class definitions
Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base and maps to states table.

    Attributes:
        id (sqlalchemy Integer): primary key, auto-incremented, non-nullable.
        name (sqlalchemy String): max 128 chars, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
