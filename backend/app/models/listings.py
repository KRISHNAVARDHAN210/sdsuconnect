from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    rent = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    date_available = Column(String, nullable=True)  # for simplicity, use string
