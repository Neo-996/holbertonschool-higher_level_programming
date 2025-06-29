#!/usr/bin/python3
"""
Defines the City class linked to the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # Import Base from model_state.py


class City(Base):
    """City class linked to 'cities' table."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
