from pydantic import BaseModel, Field
from typing import Optional

class Listing(BaseModel):
    id: int
    title: str
    user_id: str
    description: Optional[str] = None
    latitude: Optional[float] = Field(None, description="Latitude of item location")
    longitude: Optional[float] = Field(None, description="Longitude of item location")
    status: Optional[str] = "active"

# Schema for login request
class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    email: str
    password: str


# Schema for user model
class User(BaseModel):
    user_id: str
    username: str
    full_name: Optional[str] = None
    location: Optional[str] = None
    email: str
    password: str
