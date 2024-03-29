#!/usr/bin/python3
""" Defining a City class
    that Inherits from SQLAlchemy Base and links to the MySQL table cities
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Represents a city column for a MySQL table

    __tablename__ (str): MySQL table to store Cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id(sqlalchemy.Integer):  states.id foreign key
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
