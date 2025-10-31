from fastapi import APIRouter
from models.user_model import User
from database.database_service import UsersDB
from fastapi import HTTPException

from schemas import LocationUpdateRequest, LoginRequest, SignupRequest

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
async def signup(request: SignupRequest):
    print("Signup request received:", request)

    email = request.email
    
    # Check if user already exists
    users_db = UsersDB()
    
    existing_user = await users_db.get_user_by_email(email)

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists. Please log in instead.")

    password = request.password
    created_at = request.created_at
    latitude = request.latitude
    longitude = request.longitude
    
    print(f"Signup attempt for email: {email}")
    
    user = User(
        id="user_" + email,
        username=email.split("@")[0],
        email=email,
        password=password,
        created_at=created_at,
        latitude=latitude or None,
        longitude=longitude or None
    )

    await  users_db.add_user(user.model_dump())
    return {"message": "User created", "user": user.model_dump()}

@router.post("/login")
async def login(request: LoginRequest):
    email = request.email
    password = request.password

    print(f"Login attempt for email: {email}")

    users_db = UsersDB()
    stored_user = await users_db.get_user_by_email(email)

    if not stored_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if stored_user["password"] == password:
        return {"status_code": 200, "message": "Login successful", "user": stored_user}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
    # return {"message": "Invalid credentials"}

@router.get("/get_all")
async def get_users():
    users_db = UsersDB()
    users = await users_db.get_all_users()
    return users


@router.put("/update_location")
async def update_location(request: LocationUpdateRequest):
    user_id = request.user_id
    latitude = request.latitude
    longitude = request.longitude

    users_db = UsersDB()
    updated_user = await users_db.update_user_location(user_id, latitude, longitude)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Location updated", "user": updated_user}
