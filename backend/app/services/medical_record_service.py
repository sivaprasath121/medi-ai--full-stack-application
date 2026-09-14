from __future__ import annotations

MEDICAL_RECORDS = {
    "patient-001": {
        "patient_id": "patient-001",
        "patient_name": "Ava Martinez",
        "summary": "Stable cardiology follow-up; current symptoms improved.",
        "recent_events": [
            {"title": "Cardiology follow-up", "date": "2026-09-10", "type": "visit"},
            {"title": "CBC review", "date": "2026-09-08", "type": "lab"},
            {"title": "Medication adjustment", "date": "2026-08-28", "type": "prescription"},
        ],
        "diagnoses": ["Seasonal allergies", "Mild hypertension risk"],
        "providers": ["Dr. Olivia Chen", "Dr. Maya Patel"],
    },
    "patient-002": {
        "patient_id": "patient-002",
        "patient_name": "Daniel Nguyen",
        "summary": "New patient intake complete; monitoring lifestyle intervention plan.",
        "recent_events": [
            {"title": "Initial intake", "date": "2026-09-06", "type": "visit"},
            {"title": "Baseline labs", "date": "2026-09-04", "type": "lab"},
        ],
        "diagnoses": ["Asthma follow-up"],
        "providers": ["Dr. Olivia Chen"],
    },
}


def list_medical_records() -> list[dict]:
    return [
        {
            "patient_id": patient_id,
            "patient_name": record["patient_name"],
            "title": f"Record for {record['patient_name']}",
            "summary": record["summary"],
        }
        for patient_id, record in MEDICAL_RECORDS.items()
    ]


def get_medical_record(patient_id: str) -> dict | None:
    return MEDICAL_RECORDS.get(patient_id)
