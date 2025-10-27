from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

# Class representing the status of the Listing
class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SOLD = "sold"

class Listing(BaseModel):
    id: Optional[str] = None
    user_id: str
    title: str
    description: str
    created_at: str 
    status: Status
    category: str  
    latitude: Optional[float] = Field(None, description="Latitude of item location")
    longitude: Optional[float] = Field(None, description="Longitude of item location")
