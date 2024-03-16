from pydantic import MongoDsn, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: MongoDsn = ...
    mongodb_db_name: str = ...
    log_level: str = 'INFO'

    logger_filename: str = ...
    logger_maxbytes: int = 15000000
    logger_mod: str = 'a'
    logger_backup_count: int = 5


settings = Settings()
