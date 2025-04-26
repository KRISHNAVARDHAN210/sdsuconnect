from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core import database
from app.models import profile as profile_model
from app.schemas import profile as profile_schema
from app.models import user as user_model
from app.core.deps import get_current_user  

router = APIRouter()

# POST - Create Profile (NO authentication)
@router.post("/", response_model=profile_schema.ProfileOut)
def create_profile(profile: profile_schema.ProfileCreate, db: Session = Depends(database.get_db)):
    new_profile = profile_model.Profile(**profile.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

# GET - View Profile (NO authentication)
@router.get("/", response_model=profile_schema.ProfileOut)
def get_my_profile(db: Session = Depends(database.get_db), current_user: user_model.User = Depends(get_current_user)):
    profile = db.query(profile_model.Profile).filter(profile_model.Profile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/", response_model=profile_schema.ProfileOut)
def update_my_profile(profile_update: profile_schema.ProfileUpdate, db: Session = Depends(get_db), current_user: user_model.User = Depends(get_current_user)):
    profile = db.query(profile_model.Profile).filter(profile_model.Profile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    for key, value in profile_update.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)
    return profile

# DELETE - Delete Profile (NO authentication)
@router.delete("/", status_code=204)
def delete_profile(db: Session = Depends(database.get_db)):
    profile = db.query(profile_model.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    db.delete(profile)
    db.commit()
    return {"message": "Profile deleted successfully"}
