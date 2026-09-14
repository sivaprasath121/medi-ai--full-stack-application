from __future__ import annotations

APPOINTMENTS = [
    {
        "id": "appt-101",
        "patient_id": "patient-001",
        "patient_name": "Ava Martinez",
        "doctor_id": "doctor-001",
        "doctor_name": "Dr. Olivia Chen",
        "date": "2026-09-18",
        "time": "10:30",
        "reason": "Cardiology follow-up",
        "status": "scheduled",
    },
    {
        "id": "appt-102",
        "patient_id": "patient-002",
        "patient_name": "Daniel Nguyen",
        "doctor_id": "doctor-001",
        "doctor_name": "Dr. Olivia Chen",
        "date": "2026-09-18",
        "time": "11:15",
        "reason": "New patient intake",
        "status": "confirmed",
    },
]


def list_appointments() -> list[dict]:
    return APPOINTMENTS


def create_appointment(payload: dict) -> dict:
    patient_name = {
        "patient-001": "Ava Martinez",
        "patient-002": "Daniel Nguyen",
    }.get(payload["patient_id"], "Unknown Patient")

    doctor_name = {
        "doctor-001": "Dr. Olivia Chen",
    }.get(payload["doctor_id"], "Unknown Doctor")

    appointment = {
        "id": f"appt-{len(APPOINTMENTS) + 101}",
        "patient_id": payload["patient_id"],
        "patient_name": patient_name,
        "doctor_id": payload["doctor_id"],
        "doctor_name": doctor_name,
        "date": payload["date"],
        "time": payload["time"],
        "reason": payload["reason"],
        "status": payload.get("status", "scheduled"),
    }
    APPOINTMENTS.append(appointment)
    return appointment
