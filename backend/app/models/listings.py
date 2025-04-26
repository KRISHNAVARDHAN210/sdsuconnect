from app.core.database import Base
from sqlalchemy import Column, Integer, String, Float

class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, index=True)
    building_name = Column(String)
    address = Column(String)
    campus_type = Column(String)
    price = Column(Float)
    sharing_type = Column(String)
    lease_duration = Column(String)
    availability_date = Column(String)
    listed_by = Column(String)
    lease_type = Column(String)
    space = Column(String)
