from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from ....core.db.mssql.db_connect import db_connect
from ....core.models import Operation
from .schemas import OperationCreate

router = APIRouter(tags=["Operation"])


@router.get("/")
async def get_specific_operations(
    operation_type: str,
    session: AsyncSession = Depends(db_connect),
):
    query = select(Operation).where(Operation.type_name == operation_type)
    result: Result = await session.execute(query)
    return list(result.scalars().all())


@router.post("/")
async def add_specific_operations(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(db_connect),
):
    stmt = insert(Operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
