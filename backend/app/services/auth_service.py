from __future__ import annotations

from typing import Any

from app.auth import hash_password


DEMO_USERS: dict[str, dict[str, Any]] = {
    "patient.demo@example.com": {
        "id": "patient-demo-id",
        "email": "patient.demo@example.com",
        "password_hash": hash_password("DemoPassword123!"),
        "full_name": "Maya Patel",
        "role": "patient",
    },
    "doctor.demo@example.com": {
        "id": "doctor-demo-id",
        "email": "doctor.demo@example.com",
        "password_hash": hash_password("DemoPassword123!"),
        "full_name": "Dr. Olivia Chen",
        "role": "doctor",
    },
    "admin.demo@example.com": {
        "id": "admin-demo-id",
        "email": "admin.demo@example.com",
        "password_hash": hash_password("DemoPassword123!"),
        "full_name": "Alicia Gomez",
        "role": "admin",
    },
}


def get_demo_user(email: str) -> dict[str, Any] | None:
    return DEMO_USERS.get(email)
