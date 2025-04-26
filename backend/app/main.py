from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User
from app.models.profile import Profile
from app.routes import auth, profile as profile_route

app = FastAPI()

# Important: Create tables after importing models
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_route.router, prefix="/profile", tags=["Profile"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Aztec Connect API!"}
