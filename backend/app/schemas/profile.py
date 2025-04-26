from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    hobbies: Optional[str] = None
    gender: Optional[str] = None
    languages_spoken: Optional[str] = None
    food_preference: Optional[str] = None
    existing_connections: Optional[str] = None

class ProfileCreate(ProfileBase):
    first_name: str
    last_name: str
    department: str
    student_type: str

class ProfileUpdate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    id: int
    first_name: str
    last_name: str
    department: str
    student_type: str

    class Config:
        orm_mode = True
