#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

os.environ.setdefault("APP_NAME", "MediAI")
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DATABASE_URL", "sqlite:///./medi_ai_smoke.db")
os.environ.setdefault("JWT_SECRET", "smoke-secret-change-me")

import pytest

if __name__ == "__main__":
    os.chdir(BACKEND)
    raise SystemExit(pytest.main(["tests/test_smoke.py", "-q"]))
