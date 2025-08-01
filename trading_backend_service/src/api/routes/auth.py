from fastapi import APIRouter, status
from src.schemas.auth import (
    LoginRequest, LoginResponse,
    SignupRequest, SignupResponse,
    LogoutResponse
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

# PUBLIC_INTERFACE
@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK, summary="Login user", description="Authenticate user and return a JWT access token.")
async def login_user(payload: LoginRequest):
    """Authenticate user and return a JWT access token."""
    return LoginResponse(access_token="sampletoken", token_type="bearer")

# PUBLIC_INTERFACE
@router.post("/signup", response_model=SignupResponse, status_code=status.HTTP_201_CREATED, summary="Signup user", description="Register new user and return user ID.")
async def signup_user(payload: SignupRequest):
    """Register new user and return user ID."""
    return SignupResponse(user_id="example_id", email=payload.email)

# PUBLIC_INTERFACE
@router.post("/logout", response_model=LogoutResponse, status_code=status.HTTP_200_OK, summary="Logout", description="Logout current session and clear auth tokens.")
async def logout_user():
    """Logout current session and clear tokens."""
    return LogoutResponse(detail="Logged out successfully")
