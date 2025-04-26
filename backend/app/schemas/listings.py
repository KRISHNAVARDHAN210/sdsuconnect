from pydantic import BaseModel
from typing import Optional

class ListingBase(BaseModel):
    title: str
    description: Optional[str]
    rent: int
    city: str
    contact_info: str
    date_available: Optional[str]

class ListingCreate(ListingBase):
    pass

class ListingOut(ListingBase):
    id: int

    class Config:
        orm_mode = True
