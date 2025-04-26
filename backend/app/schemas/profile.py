from pydantic import BaseModel
from typing import List

class ProfileData(BaseModel):
    name: str
    redid: str
    phone: str
    email: str
    preferred_name: str
    gender: str
    country: List[str]
    department: str
    food: List[str]
    languages: List[str]
    roommates: bool
    accommodation: bool
