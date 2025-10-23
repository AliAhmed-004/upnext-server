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

class ListingDB:
    async def add_listing(self, listing_data):
        return listing_table.insert(listing_data)

    async def get_all_listings(self):
        return listing_table.all()

    async def get_listings_by_user(self, user_id):
        ListingQuery = Query()
        return listing_table.search(ListingQuery.user_id == user_id)
