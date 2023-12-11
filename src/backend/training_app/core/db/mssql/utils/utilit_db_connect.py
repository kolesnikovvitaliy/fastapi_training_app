from itertools import zip_longest
from typing import Annotated
from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import ValidationError


class KeysErrorInString(KeyError):
    pass


class StringConnectDBType(BaseModel):
    """
    pydantic - Проверка типов данных, при выполнении функции:
    create_string_connect_db_url
    """
    driver: Annotated[str, MinLen(5)]
    username: str
    password: str
    host: Annotated[str, MinLen(7)]
    port: int
    database: str
    query: dict[str, (str | bool)] = None


class FormatStringConnectDB():
    """
    Создание строки подключения к базе данных.
    Для alembic и db_connect требуется отформатированная строка.

    driver: str = "mssql+aioodbc",
    username: str = "",
    password: str = "",
    host: str = "localhost",
    port: int = 1433,
    database: str = "",
    query: Dict[str, str | bool] | None = None,

    """
    def __init__(self, iterable: dict):
        tmp = iterable.pop("query")
        self.__dict__.update(iterable)
        self.query = tmp

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, query):
        if query is None or len(query) == 0:
            self._query = ""
        else:
            self._query = f'?{'&'.join(
                    [f'{key_query}={
                            value.replace(' ', '+')
                            if not isinstance(value, bool) else value}'
                        for key_query, value in query.items()])}'

    def __str__(self) -> str:
        return "".join(
            f"{item}{delimiter}"
            for item, delimiter in zip_longest(
                            self.__dict__.values(),
                            ("://", ":", "@", ":", "/"),
                            fillvalue=""))

    def __repr__(self) -> str:
        return str(self)


def create_string_connect_db_url(
    driver: Annotated[str, MinLen(5)] = "mssql+aioodbc",
    username: str = "",
    password: str = "",
    host: Annotated[str, MinLen(3)] = "localhost",
    port: int = 1433,
    database: str = "",
    query: dict[str, str | bool] = None,
) -> str:
    """
    Создание отформатированной строки подключения к базе данных.
    при подключении к MSSQL параметр query["driver"] - обязателен
    пример:
    query = {
        driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
        "LongAsMax": "Yes"}
    """
    if "mssql" in driver and (query is None or len(query) == 0):
        raise KeysErrorInString("Missing required parameter 'driver'")

    try:
        return str(
            FormatStringConnectDB(
                StringConnectDBType(
                    **locals()).__dict__))  # pydantic type hinding
    except ValidationError as err:
        raise err
