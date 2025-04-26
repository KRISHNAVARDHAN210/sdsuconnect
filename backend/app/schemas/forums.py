from pydantic import BaseModel

class ForumPostBase(BaseModel):
    title: str
    content: str
    posted_by: str

class ForumPostCreate(ForumPostBase):
    pass

class ForumPostOut(ForumPostBase):
    id: int

    class Config:
        orm_mode = True
