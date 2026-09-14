from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MediAI"
    environment: str = "development"
    api_v1_prefix: str = "/api"
    database_url: str = "sqlite:///./medi_ai.db"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 120
    ai_mode: str = "mock"
    llm_provider: str = "mock"
    llm_api_key: str = "demo-placeholder"
    cors_origins: str = "*"
    demo_mode: bool = True

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
        "case_sensitive": False,
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
