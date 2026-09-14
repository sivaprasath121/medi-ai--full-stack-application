from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_doctor_overview_endpoint() -> None:
    response = client.get("/api/doctors/overview")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["name"] == "Dr. Olivia Chen"
    assert payload["today_patients"] >= 1
    assert payload["appointments_today"] >= 1


def test_doctor_patient_queue_endpoint() -> None:
    response = client.get("/api/doctors/patients")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 2
    first = payload[0]
    assert "patient_name" in first
    assert "status" in first
