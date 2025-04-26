from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import profile as profile_model
from app.core.database import get_db

router = APIRouter()

@router.get("/", tags=["Roommates"])
def find_roommates(db: Session = Depends(get_db)):
    # Get all profiles who need roommates
    roommates = db.query(profile_model.Profile).filter(profile_model.Profile.need_roommates == True).all()

    if not roommates:
        raise HTTPException(status_code=404, detail="No roommates found!")

    result = []

    for profile in roommates:
        result.append({
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "city": profile.city,
            "hobbies": profile.hobbies,
            "languages_spoken": profile.languages_spoken,
            "food_preference": profile.food_preference
        })

    return {"matches": result}
