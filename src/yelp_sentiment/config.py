# src/yelp_sentiment/config.py
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    postgres_url: str
    mongo_url: str
    data_dir: Path = Path("data")
    artifacts_dir: Path = Path("artifacts")


settings = Settings()
