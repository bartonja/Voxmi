from jose import jwt

from app.core.config import settings
from app.core.security import create_access_token, decode_access_token


def test_create_access_token():
    token = create_access_token(user_id=42)

    payload = jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[settings.jwt_algorithm],
    )

    assert payload["sub"] == "42"
    assert payload["type"] == "access"
    assert "exp" in payload

def test_decode_valid_token():
    token = create_access_token(user_id=42)

    assert decode_access_token(token) == 42


def test_decode_invalid_token():
    assert decode_access_token("invalid.token.here") is None