from fastapi import HTTPException
from tinydb import TinyDB, Query

# Initialize separate tables for Firestore-like collections
db = TinyDB("mock_database.json")
users_table = db.table("users")
listing_table = db.table("listing")

class UsersDB:
    async def add_user(self, user_data):
        return users_table.insert(user_data)

    async def get_all_users(self):
        return users_table.all()

    async def get_user_by_email(self, email):
        UserQuery = Query()
        result = users_table.search(UserQuery.email == email)
        return result[0] if result else None
    
    async def update_user_location(self, user_id, latitude, longitude):
        UserQuery = Query()
        users_table.update({'latitude': latitude, 'longitude': longitude}, UserQuery.id == user_id)
        return users_table.search(UserQuery.id == user_id)[0]

class ListingDB:
    async def add_listing(self, listing_data):
        return listing_table.insert(listing_data)

    async def get_all_listings(self):
        return listing_table.all()

    async def get_listing_info_by_id(self, listing_id):
        ListingQuery = Query()
        listings = listing_table.search(ListingQuery.id == listing_id)

        if not listings:
            raise HTTPException(status_code=404, detail="No Listings Found")

        print(f"Listings found for id {listing_id}: {listings}")

        # Extract user's name from the user_id of the listing
        user_id = listings[0]['user_id']

        UsersQuery = Query()
        user_info = users_table.search(UsersQuery.id == user_id)[0]

        print(f"Found user info: {user_info}")

        return {"listings": listings, "user_name": user_info['username']}



    async def get_listings_by_user(self, user_id):
        ListingQuery = Query()
        listings = listing_table.search(ListingQuery.user_id == user_id)

        # Sort listings by creation date in descending order
        listings.sort(key=lambda x: x['created_at'], reverse=True)

        return listings
