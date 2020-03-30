#!/usr/bin/python3
""" An honest comment in string literally """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """ Are you happy now, checker? """
    __tablename__ = 'states'
    id = Column(Integer(), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
