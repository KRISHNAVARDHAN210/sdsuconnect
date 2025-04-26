from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    country: Optional[str]
    city: Optional[str]
    hobbies: Optional[str]
    gender: Optional[str]
    languages_spoken: Optional[str]
    food_preference: Optional[str]
    existing_connections: Optional[str]
    need_accommodation: Optional[bool] = False
    need_roommates: Optional[bool] = False

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