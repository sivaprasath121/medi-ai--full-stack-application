from __future__ import annotations

from fastapi import APIRouter

from app.services.doctor_service import get_doctor_overview, get_doctor_patient_queue

router = APIRouter(prefix="/api/doctors", tags=["doctors"])


@router.get("/overview")
def doctor_overview() -> dict:
    return get_doctor_overview()


@router.get("/patients")
def doctor_patient_queue() -> list[dict]:
    return get_doctor_patient_queue()
