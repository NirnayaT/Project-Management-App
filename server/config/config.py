from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
        Defines the application settings using Pydantic's BaseSettings class.
        
        The `Settings` class contains various configuration variables for the application, such as database connection details, security settings, email settings, and more. These settings are loaded from environment variables or a `.env` file.
        
        The `model_config` attribute specifies the configuration for the Pydantic settings model, including the location of the environment file and how to handle extra variables.
    """
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS : int
    RESET_TOKEN_EXPIRE_MINUTES: int
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_FROM_NAME: str
    MAIL_SERVER : str
    MAIL_SSL_TLS: bool = False
    MAIL_STARTTLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
