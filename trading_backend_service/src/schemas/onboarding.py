from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

# PUBLIC_INTERFACE
class OnboardingRequest(BaseModel):
    """Onboarding data for user profile setup."""
    email: EmailStr
    full_name: str
    agreed_terms: bool

# PUBLIC_INTERFACE
class OnboardingResponse(BaseModel):
    message: str

# PUBLIC_INTERFACE
class KYCStartRequest(BaseModel):
    """Trigger KYC workflow for user."""
    user_id: str

# PUBLIC_INTERFACE
class KYCQuestionnaire(BaseModel):
    """KYC/risk questionnaire data structure."""
    questions: List[str]
    user_answers: Optional[List[str]] = Field(default=None)

# PUBLIC_INTERFACE
class KYCSubmitRequest(BaseModel):
    user_id: str
    answers: List[str]

# PUBLIC_INTERFACE
class KYCStatusResponse(BaseModel):
    status: str  # e.g. "pending", "verified", "rejected"
    detail: Optional[str]
