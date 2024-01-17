"""
    Contains a class definition of a state and an instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """ Class representing some state with id and name as attributes
        Inherits from Base and links to MySQL table states
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
      
