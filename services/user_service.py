from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.models import UsersRegistration
from schemas.user_schema import RegisterRequest, LoginRequest
from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)


def register_user(db: Session, data: RegisterRequest):
    if data.password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    existing_user = (
        db.query(UsersRegistration)
        .filter(UsersRegistration.email == data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = UsersRegistration(
        full_name=data.full_name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User registered successfully"}

def login_user(db: Session, data: LoginRequest):
    user = (
        db.query(UsersRegistration)
        .filter(UsersRegistration.email == data.email)
        .first()
    )

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {"user_id": user.id, "email": user.email}

    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload),
        "token_type": "bearer"
    }
