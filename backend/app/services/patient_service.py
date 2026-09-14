from __future__ import annotations

from app.models.patient import PatientProfile

PATIENTS = {
    "patient-001": PatientProfile(
        id="patient-001",
        patient_id="PT-1001",
        first_name="Ava",
        last_name="Martinez",
        email="ava.martinez@example.com",
        phone="555-0134",
        date_of_birth="1995-04-18",
        gender="Female",
        address="1480 Harbor Lane, Seattle, WA",
        emergency_contact={
            "name": "Luis Martinez",
            "relationship": "Spouse",
            "phone": "555-0140",
        },
        allergies=["Penicillin", "Peanuts"],
        current_medications=["Vitamin D", "Levothyroxine"],
        previous_conditions=["Seasonal allergies"],
        surgical_history=["Appendectomy (2018)"],
        family_history=["Mother: hypertension", "Father: type 2 diabetes"],
    ),
    "patient-002": PatientProfile(
        id="patient-002",
        patient_id="PT-1002",
        first_name="Daniel",
        last_name="Nguyen",
        email="daniel.nguyen@example.com",
        phone="555-2221",
        date_of_birth="1987-11-09",
        gender="Male",
        address="214 Pine Street, Portland, OR",
        emergency_contact={
            "name": "Jasmine Nguyen",
            "relationship": "Sibling",
            "phone": "555-2233",
        },
        allergies=["Latex"],
        current_medications=["Metformin"],
        previous_conditions=["Asthma"],
        surgical_history=["Tonsillectomy (2004)"],
        family_history=["Mother: asthma"],
    ),
}


def list_patients() -> list[dict]:
    return [
        {
            "id": patient.id,
            "patient_id": patient.patient_id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "email": patient.email,
            "gender": patient.gender,
            "date_of_birth": patient.date_of_birth,
            "summary": patient.summary,
        }
        for patient in PATIENTS.values()
    ]


def get_patient(patient_id: str) -> PatientProfile | None:
    return PATIENTS.get(patient_id)


def update_patient(patient_id: str, updates: dict) -> PatientProfile | None:
    patient = PATIENTS.get(patient_id)
    if not patient:
        return None

    for key, value in updates.items():
        if hasattr(patient, key):
            setattr(patient, key, value)
    return patient
