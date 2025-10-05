from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from .database import engine, SessionLocal

app = FastAPI()

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI + SQLite!"}
