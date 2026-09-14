from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_demo_patient_login() -> None:
    response = client.post(
        "/api/auth/login",
        json={
            "email": "patient.demo@example.com",
            "password": "DemoPassword123!",
        },
    )

    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["role"] == "patient"
    assert payload["access_token"]
    assert payload["refresh_token"]


def test_register_rejects_admin_role() -> None:
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Unauthorized Admin",
            "email": "admin.invalid@example.com",
            "password": "PassWord123!",
            "phone": "555-0123",
            "date_of_birth": "1988-05-12",
            "role": "admin",
        },
    )

    assert response.status_code == 400
    assert "Only patient and doctor roles" in response.json()["detail"]


def test_admin_route_requires_admin_role() -> None:
    login_response = client.post(
        "/api/auth/login",
        json={
            "email": "patient.demo@example.com",
            "password": "DemoPassword123!",
        },
    )
    token = login_response.json()["access_token"]

    response = client.get(
        "/api/auth/admin-only",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403
