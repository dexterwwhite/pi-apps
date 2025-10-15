from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from .database import engine, SessionLocal
from .routes import router

app = FastAPI(title="Password Manager API")

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Hello from FastAPI + SQLite!"}
