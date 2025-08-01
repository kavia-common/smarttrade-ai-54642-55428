from pydantic import BaseModel, EmailStr, Field

# PUBLIC_INTERFACE
class LoginRequest(BaseModel):
    """Login credentials."""
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=8, description="User password")

# PUBLIC_INTERFACE
class LoginResponse(BaseModel):
    """Login response with access token."""
    access_token: str = Field(..., description="JWT authentication token")
    token_type: str = Field(default="bearer", description="'bearer' for JWT tokens")

# PUBLIC_INTERFACE
class SignupRequest(BaseModel):
    """Signup request schema."""
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=8)
    full_name: str = Field(...)

# PUBLIC_INTERFACE
class SignupResponse(BaseModel):
    """Signup response schema."""
    user_id: str = Field(..., description="Registered user ID")
    email: EmailStr = Field(...)

# PUBLIC_INTERFACE
class LogoutRequest(BaseModel):
    """Logout request (may contain device/session info)."""
    pass

# PUBLIC_INTERFACE
class LogoutResponse(BaseModel):
    """Logout confirmation."""
    detail: str = Field(..., example="Logged out successfully")
