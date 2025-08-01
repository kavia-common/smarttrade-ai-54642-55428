"""
Stub authentication provider for JWT/OAuth2.
"""

from typing import Optional

# PUBLIC_INTERFACE
class AuthProvider:
    """
    Handles token issuance and validation.
    This is a stub for actual JWT/OAuth2 integration (e.g., FastAPI Security).
    """

    def authenticate(self, email: str, password: str) -> Optional[str]:
        """
        Authenticate a user and return a JWT token (stub).
        """
        # In real implementation, check password and issue JWT.
        return "mock.jwt.token"

    def verify_token(self, token: str) -> Optional[str]:
        """
        Validate JWT token, return user_id if valid (stub).
        """
        # In real implementation, decode token and verify.
        return "mock_user_id"
