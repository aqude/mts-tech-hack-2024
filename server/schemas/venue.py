import uuid
from pydantic import BaseModel


class VenueBaseModelResponse(BaseModel):
    id: uuid.UUID


class VenueResponseCreate(VenueBaseModelResponse):
    title: str
    address: str
    city_id: int


class VenueResponse(VenueResponseCreate):
    events: list


class VenueRequest(BaseModel):
    title: str
    address: str
    city_id: int


class VenueUpdateRequest(VenueRequest):
    id: uuid.UUID
