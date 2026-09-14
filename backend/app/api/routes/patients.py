from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user, require_role
from app.services.real_patient_service import create_patient, get_patient_by_id, list_patients, update_patient_record

router = APIRouter(prefix="/api", tags=["patients"])


@router.get("/patients")
def get_patients(_: dict = Depends(get_current_user)) -> list[dict]:
    return [
        {
            "id": patient.id,
            "patient_number": patient.patient_number,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "email": patient.email,
            "phone": patient.phone,
            "date_of_birth": patient.date_of_birth,
            "gender": patient.gender,
            "address": patient.address,
        }
        for patient in list_patients()
    ]


@router.post("/patients", status_code=status.HTTP_201_CREATED)
def create_patient_profile(payload: dict, _: dict = Depends(require_role("doctor", "admin"))) -> dict:
    patient = create_patient(payload)
    return {
        "id": patient.id,
        "patient_number": patient.patient_number,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "email": patient.email,
    }


@router.get("/patients/{patient_id}")
def get_patient_profile(patient_id: str, _: dict = Depends(get_current_user)) -> dict:
    patient = get_patient_by_id(patient_id)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return {
        "id": patient.id,
        "patient_number": patient.patient_number,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "email": patient.email,
        "phone": patient.phone,
        "date_of_birth": patient.date_of_birth,
        "gender": patient.gender,
        "address": patient.address,
        "emergency_contact_name": patient.emergency_contact_name,
        "emergency_contact_phone": patient.emergency_contact_phone,
        "allergies": patient.allergies,
        "medications": patient.medications,
        "conditions": patient.conditions,
    }


@router.put("/patients/{patient_id}")
def update_patient_profile(patient_id: str, payload: dict, _: dict = Depends(require_role("doctor", "admin"))) -> dict:
    patient = update_patient_record(patient_id, payload)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return {
        "id": patient.id,
        "patient_number": patient.patient_number,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "email": patient.email,
    }
