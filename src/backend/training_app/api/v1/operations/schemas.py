from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    quantiti: str
    figi: str
    instrument_type: str
    date: datetime
    type_name: str
