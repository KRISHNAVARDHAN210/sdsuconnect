from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import SessionLocal
from fastapi.responses import RedirectResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    form = await request.json()
    username = form.get("username")
    password = form.get("password")
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return RedirectResponse(url="/profile", status_code=303)
