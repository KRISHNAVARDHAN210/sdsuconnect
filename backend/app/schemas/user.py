from pydantic import BaseModel, EmailStr, constr, validator

class UserCreate(BaseModel):
    redid: str
    email: str
    password: str

class UserLogin(BaseModel):
    redid: str
    password: str

class UserOut(BaseModel):
    id: int
    redid: str
    email: str
    role: str

    class Config:
        orm_mode = True