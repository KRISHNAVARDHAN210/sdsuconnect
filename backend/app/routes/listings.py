from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.listings import Listing
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

@router.get("/nest", response_class=HTMLResponse)
async def nest_page(request: Request):
    return templates.TemplateResponse("nest.html", {"request": request})

@router.get("/listings")
async def get_listings(campus: str = "", db: Session = Depends(get_db)):
    query = db.query(Listing)
    if campus:
        query = query.filter(Listing.campus_type == campus)
    listings = query.all()
    return [{
        "id": l.id,
        "building": l.building_name,
        "address": l.address,
        "campus": l.campus_type,
        "price": l.price,
        "sharing_type": l.sharing_type,
        "lease_duration": l.lease_duration,
        "availability_date": l.availability_date,
        "listed_by": l.listed_by,
        "lease_type": l.lease_type,
        "space": l.space
    } for l in listings]

@router.post("/create_listing")
async def create_listing(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    new_listing = Listing(
        building_name=data['building_name'],
        address=data['address'],
        campus_type=data['campus_type'],
        price=data['price'],
        sharing_type=data['sharing_type'],
        lease_duration=data['lease_duration'],
        availability_date=data['availability_date'],
        listed_by=data['listed_by'],
        lease_type=data['lease_type'],
        space=data['space']
    )
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return JSONResponse(content={"message": "Listing created successfully!"})
