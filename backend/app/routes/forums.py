from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.forums import ForumPost
from app.schemas import forums as forum_schema
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=forum_schema.ForumPostOut)
def create_forum_post(post: forum_schema.ForumPostCreate, db: Session = Depends(get_db)):
    new_post = ForumPost(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[forum_schema.ForumPostOut])
def get_all_forum_posts(db: Session = Depends(get_db)):
    posts = db.query(ForumPost).all()
    return posts
