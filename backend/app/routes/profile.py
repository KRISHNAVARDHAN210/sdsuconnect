from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core import database, security
from app.schemas import user as user_schema
from app.schemas import profile as profile_schema
from app.models import user as user_model
from app.core.deps import get_current_user
from datetime import timedelta



router = APIRouter()

@router.put("/", response_model=profile_schema.ProfileOut)
def update_my_profile(profile: profile_schema.ProfileUpdate, db: Session = Depends(database.get_db), current_user: user_model.User = Depends(get_current_user)):
    if not current_user.profile:
        raise HTTPException(status_code=404, detail="Profile not found.")

    for key, value in profile.dict(exclude_unset=True).items():
        setattr(current_user.profile, key, value)

    db.commit()
    db.refresh(current_user.profile)
    return current_user.profile
