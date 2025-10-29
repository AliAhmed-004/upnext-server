from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    username: str
    email: str
    password: str
    created_at: str

    # Location fields
    latitude: Optional[float] = None
    longitude: Optional[float] = None
