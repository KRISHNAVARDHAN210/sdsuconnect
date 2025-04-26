from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import auth 
from app.models import user, profile  # Import models so tables are created
from app.routes import auth, profile as profile_route 

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_route.router, prefix="/profile", tags=["Profile"])


@app.get("/")
def read_root():
    return {"message": "Welcome to SDSUConnect API!"}
