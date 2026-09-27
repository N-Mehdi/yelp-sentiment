from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# config.py -> yelp_sentiment/ -> src/ -> racine du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")

    postgres_url: str
    mongo_url: str
    data_dir: Path = PROJECT_ROOT / "data"
    artifacts_dir: Path = PROJECT_ROOT / "artifacts"


settings = Settings()
