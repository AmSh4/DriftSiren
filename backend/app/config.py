from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    POSTGRES_USER: str = "driftsiren"
    POSTGRES_PASSWORD: str = "driftsiren"
    POSTGRES_DB: str = "driftsiren"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    REDIS_URL: str = "redis://redis:6379/0"
    SECRET_KEY: str = "dev-secret-change-me"
    CORS_ORIGINS: str = "http://localhost:3000"

    BACKEND_URL: str = "http://localhost:8000"

    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings()  # Loads from env
