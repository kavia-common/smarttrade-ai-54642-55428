from typing import Optional
from pydantic import BaseModel, EmailStr

# PUBLIC_INTERFACE
class UpdateSettingsRequest(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    notifications_enabled: Optional[bool] = True

# PUBLIC_INTERFACE
class UpdateSettingsResponse(BaseModel):
    status: str
    detail: Optional[str]

# PUBLIC_INTERFACE
class APIKeyCreateResponse(BaseModel):
    api_key: str

# PUBLIC_INTERFACE
class APIKeyRevokeRequest(BaseModel):
    api_key_id: str

# PUBLIC_INTERFACE
class APIKeyListResponse(BaseModel):
    api_keys: list
