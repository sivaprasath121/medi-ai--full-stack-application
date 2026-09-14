from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_medical_records() -> None:
    response = client.get("/api/medical-records")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    assert payload[0]["title"]


def test_get_patient_medical_record() -> None:
    response = client.get("/api/medical-records/patient-001")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["patient_id"] == "patient-001"
    assert payload["recent_events"]
