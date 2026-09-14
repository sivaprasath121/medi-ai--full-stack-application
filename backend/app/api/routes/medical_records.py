from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user, require_role
from app.services.real_medical_record_service import create_medical_record, get_medical_record_by_patient, list_medical_records

router = APIRouter(prefix="/api", tags=["medical-records"])


@router.get("/medical-records")
def get_records(_: dict = Depends(get_current_user)) -> list[dict]:
    return [
        {
            "id": record.id,
            "patient_id": record.patient_id,
            "title": record.title,
            "summary": record.summary,
            "diagnosis": record.diagnosis,
            "provider_name": record.provider_name,
        }
        for record in list_medical_records()
    ]


@router.post("/medical-records", status_code=status.HTTP_201_CREATED)
def create_record(payload: dict, _: dict = Depends(require_role("doctor", "admin"))) -> dict:
    record = create_medical_record(payload)
    return {
        "id": record.id,
        "patient_id": record.patient_id,
        "title": record.title,
        "summary": record.summary,
        "diagnosis": record.diagnosis,
        "provider_name": record.provider_name,
    }


@router.get("/medical-records/{patient_id}")
def get_record(patient_id: str, _: dict = Depends(get_current_user)) -> dict:
    record = get_medical_record_by_patient(patient_id)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
    return {
        "id": record.id,
        "patient_id": record.patient_id,
        "title": record.title,
        "summary": record.summary,
        "diagnosis": record.diagnosis,
        "provider_name": record.provider_name,
    }
