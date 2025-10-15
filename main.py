
from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Listing, LoginRequest, User

app = FastAPI(title="UpNext API")

# In-memory "database"
listings = [
    Listing(id=1, title="Fix leaking faucet", description="Local plumber needed", user_id="user1"),
    Listing(id=2, title="UI/UX Designer Wanted", description="For a Flutter startup", user_id="user2"),
]

# In-memory user data
users = {
        "user1": {"user_id": "user_1", "username": "user1", "full_name": "User One", "email": "user1@email.com", "password": "password"},
        "user2": {"user_id": "user_2", "username": "user2", "full_name": "User Two", "email": "user2@email.com", "password": "password2"},
}

# LISTINGS ENDPOINTS
@app.get("/api/listings")
def get_listings():
    return listings

@app.get("/api/listings/{listing_id}", response_model=Listing)
def get_listing(listing_id: int):
    for listing in listings:
        if listing.id == listing_id:
            return listing
    raise HTTPException(status_code=404, detail="Listing not found")

@app.post("/api/listings", response_model=Listing)
def add_listing(listing: Listing):
    listings.append(listing)
    return listing

@app.delete("/api/listings/{listing_id}")
def delete_listing(listing_id: int):
    global listings
    listings = [l for l in listings if l.id != listing_id]
    return {"message": f"Listing {listing_id} deleted"}


# USERS ENDPOINTS
@app.post("/api/auth/login")
def login(request: LoginRequest):
    email = request.email
    password = request.password

    print(f"Attempting login for user: {email}")
    print(f"Provided password: {password}")

    
    # extract user with matching email
    user = next((u for u in users if users[u]["email"] == email), None)

    if user:
        print(f"User found: {user}")
        if users[user]["password"] == password:
            print("Password match")
            return {"message": "Login successful", "user": users[user]}
        else:
            print("Password mismatch")
    else:
        print("User not found")
    raise HTTPException(status_code=401, detail="Invalid username or password")
