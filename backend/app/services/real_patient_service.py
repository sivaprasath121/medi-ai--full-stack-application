from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.patient import Patient


def create_patient(payload: dict) -> Patient:
    db = SessionLocal()
    try:
        patient = Patient(
            patient_number=payload["patient_number"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            email=payload["email"],
            phone=payload.get("phone"),
            date_of_birth=payload.get("date_of_birth"),
            gender=payload.get("gender"),
            address=payload.get("address"),
            emergency_contact_name=payload.get("emergency_contact_name"),
            emergency_contact_phone=payload.get("emergency_contact_phone"),
            allergies=payload.get("allergies"),
            medications=payload.get("medications"),
            conditions=payload.get("conditions"),
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient
    finally:
        db.close()


def list_patients() -> list[Patient]:
    db = SessionLocal()
    try:
        return db.execute(select(Patient).order_by(Patient.created_at.desc())).scalars().all()
    finally:
        db.close()


def get_patient_by_id(patient_id: str) -> Patient | None:
    db = SessionLocal()
    try:
        return db.get(Patient, patient_id)
    finally:
        db.close()


def update_patient_record(patient_id: str, payload: dict) -> Patient | None:
    db = SessionLocal()
    try:
        patient = db.get(Patient, patient_id)
        if patient is None:
            return None
        for key, value in payload.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        db.commit()
        db.refresh(patient)
        return patient
    finally:
        db.close()
