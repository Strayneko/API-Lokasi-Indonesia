from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    DB: str
    DB_POOL_PRE_PING: bool = True
    DB_POOL_RECYCLE: int = 1800
    DB_ECHO: bool = False

    class Config:
        env_file = '.env'


@lru_cache
def get_config():
    return Config()


config = get_config()
