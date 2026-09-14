from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import create_access_token, get_current_user, hash_password, require_role, verify_password
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.auth import LoginRequest, PasswordResetRequest, RegisterRequest, ResetPasswordRequest, TokenResponse
from app.services.auth_service import get_demo_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: RegisterRequest, db: Session = Depends(get_db)) -> TokenResponse:
    if payload.role not in {UserRole.PATIENT.value, UserRole.DOCTOR.value}:
        raise HTTPException(status_code=400, detail="Only patient and doctor roles are allowed for self-registration")

    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already registered")

    user = User(
        full_name=payload.full_name,
        email=str(payload.email),
        password_hash=hash_password(payload.password),
        phone=payload.phone,
        date_of_birth=payload.date_of_birth,
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return TokenResponse(
        access_token=create_access_token(str(user.id), user.role),
        refresh_token=create_access_token(str(user.id), user.role, expires_delta=10080),
        role=user.role,
        user_id=str(user.id),
    )


@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    demo_user = get_demo_user(str(payload.email))
    if demo_user and verify_password(payload.password, demo_user["password_hash"]):
        user_id = demo_user["id"]
        user_role = demo_user["role"]
        return TokenResponse(
            access_token=create_access_token(str(user_id), user_role),
            refresh_token=create_access_token(str(user_id), user_role, expires_delta=10080),
            role=user_role,
            user_id=str(user_id),
        )

    user = db.query(User).filter(User.email == str(payload.email)).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return TokenResponse(
        access_token=create_access_token(str(user.id), user.role),
        refresh_token=create_access_token(str(user.id), user.role, expires_delta=10080),
        role=user.role,
        user_id=str(user.id),
    )


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(current_user: dict = Depends(get_current_user)) -> TokenResponse:
    return TokenResponse(
        access_token=create_access_token(current_user["sub"], current_user["role"]),
        refresh_token=create_access_token(current_user["sub"], current_user["role"], expires_delta=10080),
        role=current_user["role"],
        user_id=current_user["sub"],
    )


@router.post("/logout")
def logout_user(_: dict = Depends(get_current_user)) -> dict[str, str]:
    return {"status": "logged_out"}


@router.post("/forgot-password")
def forgot_password(payload: PasswordResetRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    user = db.query(User).filter(User.email == str(payload.email)).first()
    if user is None:
        return {"status": "if_account_exists_reset_instructions_have_been_sent"}
    return {"status": "reset_link_sent"}


@router.post("/reset-password")
def reset_password(payload: ResetPasswordRequest, db: Session = Depends(get_db)) -> dict[str, str]:
    user = db.query(User).filter(User.email == str(payload.email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.password_hash = hash_password(payload.new_password)
    db.commit()
    return {"status": "password_reset_successful"}


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)) -> dict[str, str]:
    return {"user_id": current_user["sub"], "role": current_user["role"]}


@router.get("/admin-only")
def admin_only(_: dict = Depends(require_role(UserRole.ADMIN.value))) -> dict[str, str]:
    return {"status": "admin_access_ok"}
