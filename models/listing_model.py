from datetime import date
from enum import Enum
from pydantic import BaseModel
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
    location: str 
