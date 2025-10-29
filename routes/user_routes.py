from fastapi import APIRouter
from models.user_model import User
from database.database_service import UsersDB
from fastapi import HTTPException

from schemas import LoginRequest, SignupRequest

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
async def signup(request: SignupRequest):
    print("Signup request received:", request)

    email = request.email
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

    users_db = UsersDB()
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

