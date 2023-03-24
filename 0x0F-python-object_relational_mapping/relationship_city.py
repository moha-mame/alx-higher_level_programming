#!/usr/bin/python3
""" model_state module """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ City class """
    __tablename__ = "cities"
    id = Column('id', Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
