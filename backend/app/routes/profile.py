from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileData
from app.core.database import SessionLocal
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@router.post("/save_profile")
async def save_profile(profile: ProfileData, db: Session = Depends(get_db)):
    new_profile = Profile(
        user_id=1,  # (dummy user ID for now)
        name=profile.name,
        redid=profile.redid,
        phone=profile.phone,
        email=profile.email,
        preferred_name=profile.preferred_name,
        gender=profile.gender,
        country=",".join(profile.country),
        department=profile.department,
        food=",".join(profile.food),
        languages=",".join(profile.languages),
        roommates=profile.roommates,
        accommodation=profile.accommodation
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return JSONResponse(content={"message": "Profile saved successfully!"})
