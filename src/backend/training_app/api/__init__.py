from fastapi import APIRouter

from .v1.operations.views import router as router_operations
from .v1.products.views import router as router_products


router = APIRouter()

router.include_router(
    router=router_operations,
    prefix="/operations",
)

router.include_router(
    router=router_products,
    prefix="/products",
)
