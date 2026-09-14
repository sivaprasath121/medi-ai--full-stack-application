from __future__ import annotations

from sqlalchemy import select

from app.database import SessionLocal
from app.models.appointment import Appointment


def create_appointment(payload: dict) -> Appointment:
    db = SessionLocal()
    try:
        appointment = Appointment(
            patient_id=payload["patient_id"],
            doctor_id=payload["doctor_id"],
            appointment_date=payload["date"],
            appointment_time=payload["time"],
            reason=payload["reason"],
            status=payload.get("status", "scheduled"),
        )
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment
    finally:
        db.close()


def list_appointments() -> list[Appointment]:
    db = SessionLocal()
    try:
        return db.execute(select(Appointment).order_by(Appointment.created_at.desc())).scalars().all()
    finally:
        db.close()


def get_appointment_by_id(appointment_id: str) -> Appointment | None:
    db = SessionLocal()
    try:
        return db.get(Appointment, appointment_id)
    finally:
        db.close()
