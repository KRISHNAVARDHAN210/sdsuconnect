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

@router.get("/roomies", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("roomies.html", {"request": request})