from pydantic import BaseModel

class CredentialBase(BaseModel):
    title: str
    website: str
    username: str
    password: str

class CredentialCreate(CredentialBase):
    pass

class CredentialUpdate(BaseModel):
    title: str | None = None
    website: str | None = None
    username: str | None = None
    password: str | None = None

class Credential(CredentialBase):
    id: int

    class Config:
        orm_mode = True
