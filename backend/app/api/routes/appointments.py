from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user, require_role
from app.services.real_appointment_service import create_appointment, get_appointment_by_id, list_appointments

router = APIRouter(prefix="/api", tags=["appointments"])


@router.get("/appointments")
def get_appointments(_: dict = Depends(get_current_user)) -> list[dict]:
    return [
        {
            "id": item.id,
            "patient_id": item.patient_id,
            "doctor_id": item.doctor_id,
            "date": item.appointment_date,
            "time": item.appointment_time,
            "reason": item.reason,
            "status": item.status,
        }
        for item in list_appointments()
    ]


@router.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: str, _: dict = Depends(get_current_user)) -> dict:
    item = get_appointment_by_id(appointment_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
    return {
        "id": item.id,
        "patient_id": item.patient_id,
        "doctor_id": item.doctor_id,
        "date": item.appointment_date,
        "time": item.appointment_time,
        "reason": item.reason,
        "status": item.status,
    }


@router.post("/appointments", status_code=status.HTTP_201_CREATED)
def schedule_appointment(payload: dict, _: dict = Depends(require_role("doctor", "admin", "patient"))) -> dict:
    required = {"patient_id", "doctor_id", "date", "time", "reason"}
    if not required.issubset(payload.keys()):
        raise HTTPException(status_code=400, detail="Missing required appointment fields")
    item = create_appointment(payload)
    return {
        "id": item.id,
        "patient_id": item.patient_id,
        "doctor_id": item.doctor_id,
        "date": item.appointment_date,
        "time": item.appointment_time,
        "reason": item.reason,
        "status": item.status,
    }
