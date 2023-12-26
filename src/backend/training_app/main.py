import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi_cache.decorator import cache
from .core.db.redis_cache.init_redis_cache import redis_cache

from .auth import router as router_auth
from .api import router as router_v1
from .core.db.mssql.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_cache()
    yield


app = FastAPI(title="Training App", lifespan=lifespan)
app.include_router(router=router_auth)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@cache()
async def get_cache():
    return 1


@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
