#!/usr/bin/python3
"""Defines State, inherits from Base, and links to MySQL table states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
	"""state for MySQL db"""
	__tablename__ = "states"
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
