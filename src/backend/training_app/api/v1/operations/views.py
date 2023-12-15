import time
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from ....core.db.mssql.db_connect import db_connect
from ....core.models import Operation
from .schemas import OperationCreate

router = APIRouter(tags=["Operation"])

@router.get("/long_operation")
@cache(expire=120)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"

@router.get("/")
async def get_specific_operations(
    operation_type: str,
    session: AsyncSession = Depends(db_connect),
):
    try:
        query = select(Operation).where(Operation.type_name == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": list(result.scalars().all()),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_specific_operations(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(db_connect),
):
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
