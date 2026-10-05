from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    postgres_db : str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @property
    def postgres_url(self) -> str:
      return(
        "postgresql+psycopg://"
        f"{self.postgres_user}:"
        f"{self.postgres_password}@"
        f"{self.postgres_host}:"
        f"{self.postgres_port}/"
        f"{self.postgres_db}"
      )

    model_config = SettingsConfigDict(
      env_file=ENV_FILE,
      extra="ignore",
    )

settings = Settings()
