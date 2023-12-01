import uvicorn

from fastapi import FastAPI


app = FastAPI(title="Trading App")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
