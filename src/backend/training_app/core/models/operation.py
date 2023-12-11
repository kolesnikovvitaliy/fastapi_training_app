from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Operation(Base):
    quantiti: Mapped[str] = mapped_column(
        String(25),
    )
    figi: Mapped[str] = mapped_column(String(50))
    instrument_type: Mapped[str] = mapped_column(String(50), nullable=True)
    date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
        nullable=False,
    )
    type_name: Mapped[str] = mapped_column(String(50))
