import uuid
from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import EmailStr

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: Annotated[str, MinLen(3), MaxLen(25)]
    first_name: Annotated[str, MinLen(3), MaxLen(50)]
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: Annotated[str, MinLen(3), MaxLen(25)]
    first_name: Annotated[str, MinLen(3), MaxLen(50)]
    role_id: int
    email: EmailStr
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
