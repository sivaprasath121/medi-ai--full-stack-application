from fastapi.testclient import TestClient

from app.auth import create_access_token
from app.main import app

client = TestClient(app)


def test_protected_routes_require_auth() -> None:
    response = client.get("/api/patients")
    assert response.status_code == 401

    token = create_access_token("patient-demo-id", "patient")
    authed = client.get("/api/patients", headers={"Authorization": f"Bearer {token}"})
    assert authed.status_code == 200


def test_patient_and_appointment_crud_persists_in_db() -> None:
    token = create_access_token("doctor-demo-id", "doctor")
    headers = {"Authorization": f"Bearer {token}"}

    create_patient = client.post(
        "/api/patients",
        json={
            "patient_number": "PT-3001",
            "first_name": "Lena",
            "last_name": "Brown",
            "email": "lena.brown@example.com",
            "phone": "555-9911",
            "date_of_birth": "1990-07-12",
            "gender": "Female",
            "address": "44 Pine Ave",
            "emergency_contact_name": "Sam Brown",
            "emergency_contact_phone": "555-9922",
            "allergies": "Peanuts",
            "medications": "Vitamin C",
            "conditions": "None",
        },
        headers=headers,
    )
    assert create_patient.status_code == 201, create_patient.text
    patient_id = create_patient.json()["id"]

    patient = client.get(f"/api/patients/{patient_id}", headers=headers)
    assert patient.status_code == 200
    assert patient.json()["first_name"] == "Lena"

    create_appointment = client.post(
        "/api/appointments",
        json={
            "patient_id": patient_id,
            "doctor_id": "doctor-demo-id",
            "date": "2026-10-01",
            "time": "15:00",
            "reason": "Follow-up",
            "status": "scheduled",
        },
        headers=headers,
    )
    assert create_appointment.status_code == 201, create_appointment.text
    appointment_id = create_appointment.json()["id"]

    appointment = client.get(f"/api/appointments/{appointment_id}", headers=headers)
    assert appointment.status_code == 200
    assert appointment.json()["reason"] == "Follow-up"
