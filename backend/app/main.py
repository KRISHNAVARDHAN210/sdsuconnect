from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.database import Base, engine
from app.routes import auth, profile, roommates, listings

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(roommates.router)
app.include_router(listings.router)
