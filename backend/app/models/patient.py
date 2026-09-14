from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class InsuranceInfo(BaseModel):
    provider: str = "BlueCross Demo Plan"
    member_id: str = "BC-889122"
    plan_type: str = "PPO"


class PatientProfile(BaseModel):
    id: str = "patient-001"
    patient_id: str = "PT-1001"
    first_name: str = "Ava"
    last_name: str = "Martinez"
    email: str = "ava.martinez@example.com"
    phone: str = "555-0134"
    date_of_birth: str = "1995-04-18"
    gender: str = "Female"
    address: str = "1480 Harbor Lane, Seattle, WA"
    emergency_contact: dict[str, str] = {
        "name": "Luis Martinez",
        "relationship": "Spouse",
        "phone": "555-0140",
    }
    allergies: list[str] = ["Penicillin", "Peanuts"]
    current_medications: list[str] = ["Vitamin D", "Levothyroxine"]
    previous_conditions: list[str] = ["Seasonal allergies"]
    surgical_history: list[str] = ["Appendectomy (2018)"]
    family_history: list[str] = ["Mother: hypertension", "Father: type 2 diabetes"]
    insurance: InsuranceInfo = InsuranceInfo()
    summary: dict[str, Any] = {
        "upcoming_appointment": "Cardiology follow-up | Tue 10:30 AM",
        "current_medications_count": 2,
        "last_lab_result": "CBC within normal range",
        "risk_level": "Low",
    }


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    date_of_birth: Mapped[str | None] = mapped_column(String(50), nullable=True)
    gender: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address: Mapped[str | None] = mapped_column(String(500), nullable=True)
    emergency_contact_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    emergency_contact_phone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    allergies: Mapped[str | None] = mapped_column(String(500), nullable=True)
    medications: Mapped[str | None] = mapped_column(String(500), nullable=True)
    conditions: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
