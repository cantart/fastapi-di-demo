import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

MONO_REPO_MODE = os.getenv("MONO_REPO_MODE", "false").lower() == "true"
print(f"MONO_REPO_MODE: {MONO_REPO_MODE}")

class AwsSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="aws_")

    access_key_id: str
    secret_access_key: str


class Settings(BaseSettings):
    app_prefix: str = "app2"
    model_config = SettingsConfigDict(env_prefix=f"{app_prefix}_") if MONO_REPO_MODE else SettingsConfigDict()
    
    aws: AwsSettings = AwsSettings()
    environment: str