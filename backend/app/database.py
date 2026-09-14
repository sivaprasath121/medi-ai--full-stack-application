from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings

settings = get_settings()

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def _seed_demo_users() -> None:
    from app.auth import hash_password
    from app.models.user import User

    db = SessionLocal()
    try:
        count = db.query(User).count()
        if count > 0:
            return

        demo_users = [
            User(
                full_name="Maya Patel",
                email="patient.demo@example.com",
                password_hash=hash_password("DemoPassword123!"),
                phone="555-0101",
                role="patient",
            ),
            User(
                full_name="Dr. Olivia Chen",
                email="doctor.demo@example.com",
                password_hash=hash_password("DemoPassword123!"),
                phone="555-0102",
                role="doctor",
            ),
            User(
                full_name="Alicia Gomez",
                email="admin.demo@example.com",
                password_hash=hash_password("DemoPassword123!"),
                phone="555-0103",
                role="admin",
            ),
        ]
        db.add_all(demo_users)
        db.commit()
    finally:
        db.close()


def _seed_demo_data() -> None:
    from app.models.appointment import Appointment
    from app.models.medical_record import MedicalRecord
    from app.models.patient import Patient

    db = SessionLocal()
    try:
        if db.query(Patient).count() == 0:
            patients = [
                Patient(
                    id="patient-001",
                    patient_number="PT-1001",
                    first_name="Ava",
                    last_name="Martinez",
                    email="ava.martinez@example.com",
                    phone="555-0134",
                    date_of_birth="1995-04-18",
                    gender="Female",
                    address="1480 Harbor Lane, Seattle, WA",
                    emergency_contact_name="Luis Martinez",
                    emergency_contact_phone="555-0140",
                    allergies="Penicillin, Peanuts",
                    medications="Vitamin D, Levothyroxine",
                    conditions="Seasonal allergies",
                ),
                Patient(
                    id="patient-002",
                    patient_number="PT-1002",
                    first_name="Daniel",
                    last_name="Nguyen",
                    email="daniel.nguyen@example.com",
                    phone="555-2221",
                    date_of_birth="1987-11-09",
                    gender="Male",
                    address="214 Pine Street, Portland, OR",
                    emergency_contact_name="Jasmine Nguyen",
                    emergency_contact_phone="555-2233",
                    allergies="Latex",
                    medications="Metformin",
                    conditions="Asthma",
                ),
            ]
            db.add_all(patients)

        if db.query(Appointment).count() == 0:
            appointments = [
                Appointment(
                    id="appt-101",
                    patient_id="patient-001",
                    doctor_id="doctor-demo-id",
                    appointment_date="2026-09-18",
                    appointment_time="10:30",
                    reason="Cardiology follow-up",
                    status="scheduled",
                ),
                Appointment(
                    id="appt-102",
                    patient_id="patient-002",
                    doctor_id="doctor-demo-id",
                    appointment_date="2026-09-18",
                    appointment_time="11:15",
                    reason="New patient intake",
                    status="confirmed",
                ),
            ]
            db.add_all(appointments)

        if db.query(MedicalRecord).count() == 0:
            records = [
                MedicalRecord(
                    id="record-001",
                    patient_id="patient-001",
                    title="Cardiology follow-up",
                    summary="Stable cardiology follow-up; current symptoms improved.",
                    diagnosis="Mild hypertension risk",
                    provider_name="Dr. Olivia Chen",
                ),
                MedicalRecord(
                    id="record-002",
                    patient_id="patient-002",
                    title="Initial intake",
                    summary="New patient intake complete; monitoring lifestyle intervention plan.",
                    diagnosis="Asthma follow-up",
                    provider_name="Dr. Olivia Chen",
                ),
            ]
            db.add_all(records)

        db.commit()
    finally:
        db.close()


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    _seed_demo_users()
    _seed_demo_data()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
