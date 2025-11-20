# backend/app/utils/deps.py

from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from app.database import get_session
from app.core.security import oauth2_scheme, decode_access_token
from app.crud.user import get_user_by_email


# -----------------------------
# DB SESSION DEPENDENCY
# -----------------------------
def get_db():
    session = get_session()
    try:
        yield session
    finally:
        session.close()


# -----------------------------
# AUTHENTICATION DEPENDENCY
# -----------------------------
def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    if payload is None or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    email = payload["sub"]
    user = get_user_by_email(session, email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
