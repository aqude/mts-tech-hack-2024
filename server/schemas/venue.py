import uuid
from pydantic import BaseModel


class VenueResponse(BaseModel):
    id: uuid.UUID
    title: str
    address: str
    city_id: int
    scheme: str
