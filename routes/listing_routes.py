from fastapi import APIRouter
from models.listing_model import Listing
from database.database_service import ListingDB

router = APIRouter(prefix="/listing", tags=["Posts"])

@router.get("/get_all", response_model=list[Listing])
async def get_all_listings():
    """Retrieve all listings from the database."""
    listing_db = ListingDB()

    # Get all listings
    listings = await listing_db.get_all_listings()

    # Sort listings by creation date in descending order
    listings.sort(key=lambda x: x['created_at'], reverse=True)

    return listings

@router.post("/create", response_model=dict)
async def add_listing(listing: Listing):
    """Add a new listing to the database."""
    print("Got request to add listing:", listing)

    listing_db = ListingDB()
    
    listing_id = await listing_db.add_listing(listing.model_dump())
    
    return {"message": "Listing added", "listing_id": listing_id}


@router.get("/get_by_id/{id}", response_model=dict)
async def get_listing_by_id(id: str):
    """Retrieve listings for a specific user."""
    listing_db = ListingDB()

    # Get listings by ID
    listings = await listing_db.get_listing_info_by_id(id)

    return listings

@router.get("/get_by_user", response_model=list[Listing])
async def get_listings_by_user(user_id: str):
    """Retrieve listings for a specific user."""
    print(f"Getting listings for user_id: {user_id}")
    listing_db = ListingDB()

    # Get listings by user ID
    user_listings = await listing_db.get_listings_by_user(user_id)

    return user_listings


@router.get("/number_of_listings", response_model=dict)
async def get_number_of_listings(user_id: str):
    """Retrieve the number of listings for a specific user."""
    print(f"Getting number of listings for user_id: {user_id}")
    listing_db = ListingDB()

    # Get number of listings by user ID
    user_listings = await listing_db.get_listings_by_user(user_id)

    num_listings = len(user_listings)

    return {"user_id": user_id, "count": num_listings}
