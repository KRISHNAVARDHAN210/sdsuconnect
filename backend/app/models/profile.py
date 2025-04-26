from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)  
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    gender = Column(String)
    languages_spoken = Column(String)
    food_preferences = Column(String)

    user = relationship("User", back_populates="profile")
