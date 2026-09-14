from __future__ import annotations

from sqlalchemy import select

from app.database import SessionLocal
from app.models.medical_record import MedicalRecord


def create_medical_record(payload: dict) -> MedicalRecord:
    db = SessionLocal()
    try:
        record = MedicalRecord(
            patient_id=payload["patient_id"],
            title=payload["title"],
            summary=payload["summary"],
            diagnosis=payload.get("diagnosis"),
            provider_name=payload.get("provider_name"),
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()


def list_medical_records() -> list[MedicalRecord]:
    db = SessionLocal()
    try:
        return db.execute(select(MedicalRecord).order_by(MedicalRecord.created_at.desc())).scalars().all()
    finally:
        db.close()


def get_medical_record_by_patient(patient_id: str) -> MedicalRecord | None:
    db = SessionLocal()
    try:
        return db.execute(select(MedicalRecord).where(MedicalRecord.patient_id == patient_id)).scalar_one_or_none()
    finally:
        db.close()
