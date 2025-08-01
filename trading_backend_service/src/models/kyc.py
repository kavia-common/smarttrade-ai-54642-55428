"""
KYC (Know Your Customer) ORM model stub.
"""

from sqlalchemy import Column, String, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# PUBLIC_INTERFACE
class KYCRecord(Base):
    """KYC questionnaire/result for user."""
    __tablename__ = "kyc_records"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), index=True)
    answers = Column(JSON)
    status = Column(String)  # "pending", "verified", "rejected"
    detail = Column(String, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
