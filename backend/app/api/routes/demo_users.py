from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/api/demo", tags=["demo"])


@router.get("/accounts")
def demo_accounts() -> dict[str, dict[str, str]]:
    return {
        "patient": {
            "email": "patient.demo@example.com",
            "password": "DemoPassword123!",
            "role": "patient",
        },
        "doctor": {
            "email": "doctor.demo@example.com",
            "password": "DemoPassword123!",
            "role": "doctor",
        },
        "admin": {
            "email": "admin.demo@example.com",
            "password": "DemoPassword123!",
            "role": "admin",
        },
    }
