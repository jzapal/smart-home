import mongoengine as me
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int = 3000
    MONGO_DB_NAME: str
    MONGO_DB_HOST: str

    class Config:
        case_sensitive = True


settings = Settings()


def connect_mongodb():
    conn = me.connect(
        db=settings.MONGO_DB_NAME,
        host=f'mongodb://{settings.MONGO_DB_HOST}',
    )
    conn.server_info()
    return conn
