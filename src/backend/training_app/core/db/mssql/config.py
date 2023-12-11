from pydantic import BaseModel
from pydantic_settings import BaseSettings
from .utils.get_string_connect_db_url import REAL_MSSQL_DATABASE_URL


class DBSettings(BaseModel):
    url: str = REAL_MSSQL_DATABASE_URL
    # echo: bool = False
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DBSettings = DBSettings()


settings = Settings()
