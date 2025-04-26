from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core import database, security
from app.schemas import user as user_schema
from app.models import user as user_model
from app.core.deps import get_current_user
from datetime import timedelta



router = APIRouter()

@router.post("/register", response_model=user_schema.UserOut)
def register(new_user: user_schema.UserCreate, db: Session = Depends(database.get_db)):
    existing_redid = db.query(user_model.User).filter(user_model.User.redid == new_user.redid).first()
    if existing_redid:
        raise HTTPException(status_code=400, detail="RedID already registered")

    existing_email = db.query(user_model.User).filter(user_model.User.email == new_user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = security.get_password_hash(new_user.password)

    # Create new user
    user = user_model.User(
        redid=new_user.redid,
        email=new_user.email,
        hashed_password=hashed_password,
        role="student"
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(credentials: user_schema.UserCreate, db: Session = Depends(database.get_db)):
    user = db.query(user_model.User).filter(user_model.User.redid == credentials.redid).first()

    if not user or not security.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid RedID or password")
    
    # Set token expiry manually (e.g., 30 minutes)
    access_token_expires = timedelta(minutes=30)

    token = security.create_access_token(
        data={"sub": user.redid},
        expires_delta=access_token_expires
    )
    
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=user_schema.UserOut)
def read_users_me(current_user: user_model.User = Depends(get_current_user)):
    return current_user