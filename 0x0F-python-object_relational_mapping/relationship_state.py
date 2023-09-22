#!/usr/bin/python3
"""
Defines the State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    State class to represent a state in the USA.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = \
        relationship(
            "City",
            back_populates="state",
            cascade="all,
            delete-orphan"
        )
