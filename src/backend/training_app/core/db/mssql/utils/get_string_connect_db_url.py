import os
from dotenv import load_dotenv

from .utilit_db_connect import create_string_connect_db_url

load_dotenv()


mssql_string_connect_db_url = create_string_connect_db_url(
    driver="mssql+aioodbc",
    username=os.environ.get("DB_USER", default="admin"),
    password=os.environ.get("DB_PASSWORD", default="TestTest12345678"),
    host=os.environ.get("DB_HOST", default="localhost"),
    port=int(os.environ.get("DB_PORT", default=1433)),
    database=os.environ.get("REAL_DB", default="training_app_db"),
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
        "LongAsMax": "Yes",
        # "authentication": "ActiveDirectoryIntegrated",
        "autocommit": False,
        "isolation_level": "AUTOCOMMIT",
        "fast_executemany": True,
        "ignore_no_transaction_on_rollback": True,
    },
)


REAL_MSSQL_DATABASE_URL = mssql_string_connect_db_url