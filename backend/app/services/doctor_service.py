from __future__ import annotations

DOCTOR_OVERVIEW = {
    "id": "doctor-001",
    "name": "Dr. Olivia Chen",
    "specialty": "Cardiology",
    "clinic_status": "On schedule",
    "today_patients": 18,
    "appointments_today": 12,
    "pending_reviews": 6,
    "avg_wait_time": "14 min",
    "next_round": "10:30 AM",
}

DOCTOR_PATIENT_QUEUE = [
    {
        "patient_id": "patient-001",
        "patient_name": "Ava Martinez",
        "time": "10:30 AM",
        "status": "In consultation",
        "visit_type": "Follow-up",
        "priority": "High",
    },
    {
        "patient_id": "patient-002",
        "patient_name": "Daniel Nguyen",
        "time": "11:00 AM",
        "status": "Awaiting intake",
        "visit_type": "New patient",
        "priority": "Medium",
    },
    {
        "patient_id": "patient-003",
        "patient_name": "Sofia Patel",
        "time": "11:30 AM",
        "status": "Lab review",
        "visit_type": "Check-in",
        "priority": "Normal",
    },
]


def get_doctor_overview() -> dict:
    return DOCTOR_OVERVIEW


def get_doctor_patient_queue() -> list[dict]:
    return DOCTOR_PATIENT_QUEUE
