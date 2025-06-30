#!/usr/bin/python3
"""
Defines the State class mapped to the 'states' table in a MySQL database.
Also creates the Base instance for SQLAlchemy ORM mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    
    """
    Represents the 'states' table.
    Each instance corresponds to a row in the table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
