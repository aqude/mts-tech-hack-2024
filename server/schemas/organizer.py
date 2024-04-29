import uuid
from pydantic import BaseModel


class OrganizerResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str


class OrganizerRequest(BaseModel):
    name: str
    description: str


class OrganizerUpdateRequest(BaseModel):
    id: uuid.UUID
    name: str
    description: str
