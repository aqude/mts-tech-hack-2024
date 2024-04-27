from datetime import datetime
import uuid
from pydantic import BaseModel
from .venue import VenueResponse
from .organizer import OrganizerResponse


class EventResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    date: datetime
    venue: VenueResponse
    organizer: OrganizerResponse
    tickets: int
