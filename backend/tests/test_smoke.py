from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def login_as(role: str) -> dict:
    email = {
        "patient": "patient.demo@example.com",
        "doctor": "doctor.demo@example.com",
        "admin": "admin.demo@example.com",
    }[role]
    response = client.post(
        "/api/auth/login",
        json={
            "email": email,
            "password": "DemoPassword123!",
        },
    )
    assert response.status_code == 200, response.text
    return response.json()


def test_smoke_health_and_root() -> None:
    health = client.get("/health")
    assert health.status_code == 200, health.text
    assert health.json()["status"] == "ok"

    root = client.get("/")
    assert root.status_code == 200, root.text
    assert "MediAI" in root.json()["message"]


def test_smoke_auth_login_and_role() -> None:
    payload = login_as("patient")
    assert payload["role"] == "patient"
    assert payload["access_token"]
    assert payload["refresh_token"]


def test_smoke_patient_flow() -> None:
    token = login_as("patient")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    patients = client.get("/api/patients", headers=headers)
    assert patients.status_code == 200, patients.text
    patient_list = patients.json()
    assert isinstance(patient_list, list)
    assert len(patient_list) >= 1

    patient = client.get("/api/patients/patient-001", headers=headers)
    assert patient.status_code == 200, patient.text
    payload = patient.json()
    assert payload["id"] == "patient-001"
    assert payload["patient_number"] == "PT-1001"


def test_smoke_doctor_and_appointments_flow() -> None:
    overview = client.get("/api/doctors/overview")
    assert overview.status_code == 200, overview.text
    overview_payload = overview.json()
    assert overview_payload["name"] == "Dr. Olivia Chen"

    queue = client.get("/api/doctors/patients")
    assert queue.status_code == 200, queue.text
    assert isinstance(queue.json(), list)
    assert len(queue.json()) >= 2

    token = login_as("doctor")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    appointments = client.get("/api/appointments", headers=headers)
    assert appointments.status_code == 200, appointments.text
    assert isinstance(appointments.json(), list)

    created = client.post(
        "/api/appointments",
        json={
            "patient_id": "patient-001",
            "doctor_id": "doctor-demo-id",
            "date": "2026-09-22",
            "time": "14:00",
            "reason": "Smoke test follow-up",
            "status": "scheduled",
        },
        headers=headers,
    )
    assert created.status_code == 201, created.text
    assert created.json()["status"] == "scheduled"


def test_smoke_medical_records_flow() -> None:
    token = login_as("doctor")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    records = client.get("/api/medical-records", headers=headers)
    assert records.status_code == 200, records.text
    assert isinstance(records.json(), list)
    assert len(records.json()) >= 1

    one_record = client.get("/api/medical-records/patient-001", headers=headers)
    assert one_record.status_code == 200, one_record.text
    payload = one_record.json()
    assert payload["patient_id"] == "patient-001"
    assert payload["summary"]
