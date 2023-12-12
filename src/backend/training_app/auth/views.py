import uuid
from fastapi import APIRouter, Depends

from ..core.models import User
from fastapi_users import FastAPIUsers
from .schemas import UserCreate, UserRead

from .base_config import auth_backend
from .manager import get_user_manager

router = APIRouter(tags=["Auth"])

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)

current_user = fastapi_users.current_user()


@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@router.get("/unprotected-route")
def unprotected_route():
    return "Hello, anonym"
