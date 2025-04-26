from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user
from app.routes import auth 

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def read_root():
    return {"message": "Welcome to SDSUConnect API!"}
