from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    student_type = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    hobbies = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    languages_spoken = Column(String, nullable=True)
    food_preference = Column(String, nullable=True)
    existing_connections = Column(String, nullable=True)

    need_accommodation = Column(Boolean, default=False)
    need_roommates = Column(Boolean, default=False)

    user = relationship("app.models.user.User", back_populates="profile")
