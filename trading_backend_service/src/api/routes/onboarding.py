from fastapi import APIRouter, status
from src.schemas.onboarding import (
    OnboardingRequest, OnboardingResponse,
    KYCStartRequest, KYCQuestionnaire,
    KYCSubmitRequest, KYCStatusResponse
)

router = APIRouter(
    prefix="/api/onboarding",
    tags=["Onboarding & KYC"],
)

# PUBLIC_INTERFACE
@router.post("/", response_model=OnboardingResponse, status_code=status.HTTP_200_OK, summary="Start onboarding", description="Start onboarding for a new user.")
async def onboarding(data: OnboardingRequest):
    """Register basic user and set onboarding flag."""
    return OnboardingResponse(message="Onboarding started")

# PUBLIC_INTERFACE
@router.post("/kyc/start", response_model=KYCQuestionnaire, summary="Start KYC questionnaire", description="Initiate KYC flow and get questions.")
async def kyc_start(payload: KYCStartRequest):
    """Send user the KYC/risk questionnaire."""
    return KYCQuestionnaire(questions=["Q1", "Q2"], user_answers=None)

# PUBLIC_INTERFACE
@router.post("/kyc/submit", response_model=KYCStatusResponse, summary="Submit KYC", description="Submit KYC answers and get verification status.")
async def kyc_submit(payload: KYCSubmitRequest):
    """Evaluate KYC answers."""
    return KYCStatusResponse(status="pending", detail="Under review")
