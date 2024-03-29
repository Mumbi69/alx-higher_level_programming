#!/usr/bin/python3
"""
Defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class to represent a city in a state.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", foreign_keys="state_id")
