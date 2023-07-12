# -*- encoding: utf-8 -*-
# api/api.py

from fastapi import FastAPI
from api.routes import router as LocationRouter


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "✨🌏 welcome to the location API . Try /docs to learn more."
    }

app.include_router(LocationRouter, prefix="/location")
