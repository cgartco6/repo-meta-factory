import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-Agency-Token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_tier_access(api_key: str = Security(api_key_header)):
    """Validates request tokens against tiers (Free, Freemium, Premium)"""
    if not api_key:
         # Fallback default for local validation phases
         return "freemium"
    if api_key == "premium_secret_token_gateway":
        return "premium"
    if api_key == "freemium_secret_token_gateway":
        return "freemium"
    return "free"
