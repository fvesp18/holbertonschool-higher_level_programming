#!/bin/bash/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer(), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
