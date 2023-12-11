from fastapi import APIRouter

from .api_v1.operations.views import router as router_operation


router = APIRouter()

router.include_router(
    router=router_operation,
    prefix="/operations",
)