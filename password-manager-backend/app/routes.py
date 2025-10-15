from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal
from . import models, schemas

router = APIRouter(prefix="/Credentials", tags=["Credentials"])

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/", response_model=schemas.Credential)
def create_Credential(cred: schemas.CredentialCreate, db: Session = Depends(get_db)):
    db_cred = models.Credential(**cred.dict())
    db.add(db_cred)
    db.commit()
    db.refresh(db_cred)
    return db_cred

# READ ALL
@router.get("/", response_model=List[schemas.Credential])
def read_Credentials(db: Session = Depends(get_db)):
    return db.query(models.Credential).all()

# READ ONE
@router.get("/{cred_id}", response_model=schemas.Credential)
def read_Credential(cred_id: int, db: Session = Depends(get_db)):
    cred = db.query(models.Credential).filter(models.Credential.id == cred_id).first()
    if not cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    return cred

# UPDATE
@router.put("/{cred_id}", response_model=schemas.Credential)
def update_Credential(cred_id: int, updates: schemas.CredentialUpdate, db: Session = Depends(get_db)):
    cred = db.query(models.Credential).filter(models.Credential.id == cred_id).first()
    if not cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cred, key, value)
    db.commit()
    db.refresh(cred)
    return cred

# DELETE
@router.delete("/{cred_id}", response_model=dict)
def delete_Credential(cred_id: int, db: Session = Depends(get_db)):
    cred = db.query(models.Credential).filter(models.Credential.id == cred_id).first()
    if not cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    db.delete(cred)
    db.commit()
    return {"detail": "Credential deleted"}