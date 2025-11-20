# backend/app/config.py

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # ==== APP SETTINGS ====
    APP_NAME: str = "Ecommerce App"
    ENVIRONMENT: str = "development"

    # ==== SECURITY SETTINGS ====
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ==== DATABASE SETTINGS ====
    DATABASE_URL: str  # e.g., postgresql://user:password@localhost:5432/mydb

    # ==== CORS (Frontend Origin) ====
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"          # Load environment variables from .env file
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings instance so the app doesn’t reload env vars repeatedly.
    """
    return Settings()
