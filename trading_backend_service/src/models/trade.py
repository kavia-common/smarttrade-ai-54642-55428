"""
Trade ORM model stub.
"""

from sqlalchemy import Column, String, Float, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PUBLIC_INTERFACE
class Trade(Base):
    """Represents a trade (buy/sell order) placed by the user."""
    __tablename__ = "trades"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    portfolio_id = Column(String, ForeignKey("portfolios.id"))
    symbol = Column(String)
    action = Column(String)  # "buy", "sell"
    quantity = Column(Float)
    price = Column(Float, nullable=True)  # Limit/market
    status = Column(String)  # e.g. "pending", "executed"
    executed_at = Column(DateTime, nullable=True)
    extra = Column(JSON, nullable=True)
    created_at = Column(DateTime)
