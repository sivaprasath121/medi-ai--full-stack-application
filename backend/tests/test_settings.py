from app.config import Settings


def test_default_database_url_is_sqlite_for_local_dev() -> None:
    settings = Settings()
    assert settings.database_url.startswith("sqlite")
