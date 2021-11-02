from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    MQTT_HOST: AnyUrl
    MQTT_PORT: int

    class Config:
        case_sensitive = True


settings = Settings()
