from fastapi import APIRouter
from models.listing_model import Listing
from database.database_service import ListingDB

router = APIRouter(prefix="/listing", tags=["Posts"])

@router.get("/get_all", response_model=list[Listing])
async def get_all_listings():
    """Retrieve all listings from the database."""
    listing_db = ListingDB()
    posts = await listing_db.get_all_listings()
    return posts

@router.post("/create", response_model=dict)
async def add_listing(post: Listing):
    """Add a new listing to the database."""
    listing_db = ListingDB()
    listing_id = await listing_db.add_listing(post.model_dump())
    return {"message": "Listing added", "listing_id": listing_id}

