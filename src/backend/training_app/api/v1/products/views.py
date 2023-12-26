import redis
from ....celery_worker.config import stages, STAGING_TIME, REDIS_STORE_CONN_URI
from ....celery_worker.worker import move_to_next_stage
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductUpdatePartial,
)
from .dependencies import product_by_id
from ....core.db.mssql import db_connect
from . import crud

# redis_store = redis.Redis.from_url(url="redis://:TestTest12345678@redis_cache:6379/2")
redis_store = redis.Redis.from_url(url=REDIS_STORE_CONN_URI)

router = APIRouter(tags=["Product"])


@router.post("/buy/{name}")
async def buy(name: str):
    for i in range(0, 5):
        move_to_next_stage.apply_async(
            (name, stages[i]), countdown=i * STAGING_TIME)
    return True


@router.get("/status/{name}")
async def status_rate(name: str):
    return redis_store.get(name)


@router.get(path="/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_connect),
):
    return await crud.get_products(session=session)


@router.post(
    path="/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_connect),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get(path="/{product_id}/", response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


@router.put(path="/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_connect),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch(path="/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_connect),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete(path="/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_connect),
) -> None:
    await crud.delete_product(session=session, product=product)
