#!/usr/bin/env python3

"""
SQLAlchemy model named <User>
"""

from sqlalchemy import create_engine, Column, Integer, String


class User:
    """
    model for users database table
    """
    __tablename__ = "users"
    id = Column(Integer)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)
