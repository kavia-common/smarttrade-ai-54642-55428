from fastapi import APIRouter
from src.schemas.account import (
    UpdateSettingsRequest, UpdateSettingsResponse,
    APIKeyCreateResponse, APIKeyRevokeRequest,
    APIKeyListResponse
)

router = APIRouter(
    prefix="/api/account",
    tags=["Account & API Keys"]
)

# PUBLIC_INTERFACE
@router.post("/settings/update", response_model=UpdateSettingsResponse, summary="Update account settings", description="Update profile details for the user.")
async def update_settings(payload: UpdateSettingsRequest):
    return UpdateSettingsResponse(status="success", detail="Updated.")

# PUBLIC_INTERFACE
@router.post("/apikeys/create", response_model=APIKeyCreateResponse, summary="Create new API key", description="Create a new API key for broker or integration.")
async def create_apikey():
    return APIKeyCreateResponse(api_key="sample-key")

# PUBLIC_INTERFACE
@router.post("/apikeys/revoke", summary="Revoke API key", description="Revoke an existing API key.")
async def revoke_apikey(payload: APIKeyRevokeRequest):
    return {"detail": "Revoked"}

# PUBLIC_INTERFACE
@router.get("/apikeys", response_model=APIKeyListResponse, summary="List API keys", description="List all API keys for this user.")
async def list_apikeys():
    return APIKeyListResponse(api_keys=["key1", "key2"])
