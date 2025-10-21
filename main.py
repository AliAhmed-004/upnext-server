from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Listing, LoginRequest, User

app = FastAPI(title="UpNext API")

# In-memory "database"
listings = [
    Listing(id=1, title="Dining Table Chair", description="Almost new chair", user_id="user1"),
    Listing(id=2, title="Dining Table", description="abcd", user_id="user2"),
]

# In-memory user data
users = {
    "user1": {
        "user_id": "user_1", 
        "username": "wajahat", 
        "full_name": "Wajahat Itfaq", 
        "email": "wajahat@email.com", 
        "location": "Rawalpindi",
        "password": "password"
    },

    "user2": {
        "user_id": "user_2", 
        "username": "ali_ahmed", 
        "full_name": "Ali Ahmed", 
        "email": "ali@email.com", 
        "password": "password2"
    },
}

# LISTINGS ENDPOINTS
@app.get("/api/listings")
def get_listings():
    return listings



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
            raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        print("User not found")
        raiseHttpException(status_code=404, detail="No user found with this email")
