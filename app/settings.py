from pydantic_settings import BaseSettings, SettingsConfigDict


class AwsSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="aws_")

    access_key_id: str
    secret_access_key: str


class Settings(BaseSettings):
    aws: AwsSettings = AwsSettings()
    environment: str = "local"