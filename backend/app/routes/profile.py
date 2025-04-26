from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import profile as profile_model
from app.schemas import profile as profile_schema

router = APIRouter()

# CREATE Profile (POST)
@router.post("/", response_model=profile_schema.ProfileOut)
def create_profile(profile: profile_schema.ProfileCreate, db: Session = Depends(get_db)):
    new_profile = profile_model.Profile(**profile.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

# GET Profile
@router.get("/", response_model=profile_schema.ProfileOut)
def get_profile(db: Session = Depends(get_db)):
    profile = db.query(profile_model.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

# UPDATE Profile (PUT)
@router.put("/", response_model=profile_schema.ProfileOut)
def update_profile(profile_update: profile_schema.ProfileUpdate, db: Session = Depends(get_db)):
    profile = db.query(profile_model.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    for key, value in profile_update.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)
    return profile

