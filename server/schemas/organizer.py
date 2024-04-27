import uuid
from pydantic import BaseModel


class OrganizerResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str
