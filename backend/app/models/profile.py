from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    redid = Column(String)
    phone = Column(String)
    email = Column(String)
    preferred_name = Column(String)
    gender = Column(String)
    country = Column(String)
    department = Column(String)
    food = Column(String)
    languages = Column(String)
    roommates = Column(Boolean)
    accommodation = Column(Boolean)
