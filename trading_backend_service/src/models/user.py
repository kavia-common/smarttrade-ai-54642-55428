"""
User ORM model stub for SQLAlchemy/Tortoise/etc.
"""

# Example using SQLAlchemy (can be adapted for Tortoise or other ORMs as needed)
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PUBLIC_INTERFACE
class User(Base):
    """Represents a registered user in the trading platform."""
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
