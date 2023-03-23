#!/usr/bin/python3

""" relationship_state module """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """ State class """
    __tablename__ = "states"
    id = Column('id', Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, name):
        self.name = name
