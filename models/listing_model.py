from pydantic import BaseModel
from typing import Optional

class Listing(BaseModel):
    id: Optional[str] = None
    user_id: str
    title: str
    description: str
