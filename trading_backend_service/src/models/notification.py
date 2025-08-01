"""
Notification ORM model stub.
"""

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PUBLIC_INTERFACE
class Notification(Base):
    """System/user notification entity."""
    __tablename__ = "notifications"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    type = Column(String)
    content = Column(String)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime)
