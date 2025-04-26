from pydantic import BaseModel, EmailStr, constr, validator

class UserBase(BaseModel):
    redid: constr(min_length=9, max_length=9)
    email: EmailStr

    @validator('email')
    def validate_sdsu_email(cls, v):
        if not v.endswith('@sdsu.edu'):
            raise ValueError('Email must be an SDSU email ending with @sdsu.edu')
        return v

class UserCreate(UserBase):
    password: str 

class UserOut(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
