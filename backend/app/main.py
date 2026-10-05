from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Voxmi API",
    version="1.0",
)


@app.get("/")
async def api_root():
    return {"message": "Welcome to the v1 API root"}

app.include_router(api_router)