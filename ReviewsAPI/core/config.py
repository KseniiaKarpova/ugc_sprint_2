from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    host: str = ...
    port: int = ...

    model_config = SettingsConfigDict(env_prefix='redis_')


class MongoSettings(BaseSettings):
    uri: MongoDsn = ...
    db_name: str = ...
    model_config: str = SettingsConfigDict(env_prefix='mongodb_')


class LoggerSettings(BaseSettings):
    filename: str = ...
    maxbytes: str = ...
    mod: str = ...
    backup_count: str = ...
    log_level: str = ...
    model_config: str = SettingsConfigDict(env_prefix='logger_')


class Settings(BaseSettings):
    mongodb: MongoSettings = MongoSettings()
    logger: LoggerSettings = LoggerSettings()
    redis: RedisSettings = RedisSettings()

    mongodb_uri: MongoDsn = ...
    mongodb_db_name: str = ...
    log_level: str = 'INFO'

    logger_filename: str = ...
    logger_maxbytes: int = 15000000
    logger_mod: str = 'a'
    logger_backup_count: int = 5


settings = Settings()
