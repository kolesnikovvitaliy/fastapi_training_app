from .base import Base

from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column


class Role(Base):
    name: Mapped[str] = mapped_column(String(32), unique=True)
    permissions: Mapped[dict | list] = mapped_column(
        type_=JSON,
        nullable=True,
    )
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )
