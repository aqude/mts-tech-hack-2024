from pydantic import BaseModel


class VenueBaseModelResponse(BaseModel):
    id: str


class VenueResponseCreate(VenueBaseModelResponse):
    title: str
    address: str
    city_id: int


class VenueResponse(VenueResponseCreate):
    events: list
