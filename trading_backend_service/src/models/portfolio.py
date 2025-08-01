"""
Portfolio ORM model stub.
"""

from sqlalchemy import Column, String, JSON, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PUBLIC_INTERFACE
class Portfolio(Base):
    """Represents a user's investment portfolio."""
    __tablename__ = "portfolios"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)
    holdings = Column(JSON, nullable=False)  # Positions: symbol, qty, etc.
    total_value = Column(Float, default=0)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
