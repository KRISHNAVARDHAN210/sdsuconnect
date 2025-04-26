from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.listings import Listing
from app.core.database import get_db
from app.schemas import listings as listing_schema

router = APIRouter()

@router.post("/", response_model=listing_schema.ListingOut)
def create_listing(listing: listing_schema.ListingCreate, db: Session = Depends(get_db)):
    new_listing = Listing(**listing.dict())
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

@router.get("/", response_model=list[listing_schema.ListingOut])
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(Listing).all()
    return listings
