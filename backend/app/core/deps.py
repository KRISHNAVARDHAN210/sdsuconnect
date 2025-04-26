from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    print("TOKEN RECEIVED:", token.credentials)  # <--- Add this print
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD DECODED:", payload)  # <--- Add this print
        redid: str = payload.get("sub")
        if redid is None:
            print("SUB MISSING in token!")
            raise credentials_exception
    except JWTError:
        print("JWT ERROR during decoding!")
        raise credentials_exception

    user = db.query(User).filter(User.redid == redid).first()
    if user is None:
        print("User NOT found for RedID:", redid)
        raise credentials_exception
    print("USER FOUND:", user.redid)
    return user
