from fastapi.testclient import TestClient

from app.main import app
from app.models.appointment import Appointment
from app.models.medical_record import MedicalRecord
from app.models.patient import Patient


client = TestClient(app)


def test_security_headers_are_present() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers.get("x-content-type-options") == "nosniff"
    assert response.headers.get("x-frame-options") == "DENY"
    assert response.headers.get("strict-transport-security")


def test_schema_models_exist() -> None:
    assert Patient.__tablename__ == "patients"
    assert Appointment.__tablename__ == "appointments"
    assert MedicalRecord.__tablename__ == "medical_records"
