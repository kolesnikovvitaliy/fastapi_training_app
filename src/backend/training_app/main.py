# from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from .auth import router as router_auth
from .api import router as router_v1
from .core.db.mssql.config import settings

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from fastapi_cache.decorator import cache
# from redis import asyncio as aioredis

app = FastAPI(title="Trading App")
app.include_router(router=router_auth)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     redis = aioredis.from_url(
#         "redis://localhost", encoding="utf8", decode_responses=True
#     )
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#     yield


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
