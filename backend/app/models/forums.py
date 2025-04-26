from sqlalchemy import Column, Integer, String
from app.core.database import Base

class ForumPost(Base):
    __tablename__ = "forum_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    posted_by = Column(String, nullable=False)
