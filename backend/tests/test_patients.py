from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_patients() -> None:
    response = client.get("/api/patients")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    assert payload[0]["first_name"]


def test_get_patient_profile() -> None:
    response = client.get("/api/patients/patient-001")
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "patient-001"
    assert payload["patient_id"] == "PT-1001"
    assert payload["insurance"]["provider"]


def test_update_patient_profile() -> None:
    response = client.put(
        "/api/patients/patient-001",
        json={
            "phone": "555-9001",
            "address": "245 Wellness Blvd, Seattle, WA",
            "allergies": ["Penicillin"],
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["phone"] == "555-9001"
    assert payload["address"] == "245 Wellness Blvd, Seattle, WA"
    assert "Penicillin" in payload["allergies"]
