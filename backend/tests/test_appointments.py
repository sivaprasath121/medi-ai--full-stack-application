from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_appointments() -> None:
    response = client.get("/api/appointments")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 2
    assert payload[0]["patient_name"]


def test_create_appointment() -> None:
    response = client.post(
        "/api/appointments",
        json={
            "patient_id": "patient-001",
            "doctor_id": "doctor-001",
            "date": "2026-09-20",
            "time": "09:30",
            "reason": "Follow-up consultation",
            "status": "scheduled",
        },
    )

    assert response.status_code == 201, response.text
    payload = response.json()
    assert payload["patient_name"] == "Ava Martinez"
    assert payload["doctor_name"] == "Dr. Olivia Chen"
    assert payload["status"] == "scheduled"
