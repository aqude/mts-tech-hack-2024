import uuid

from pydantic import BaseModel, Field


class GlobalEventBaseModelRequest(BaseModel):
    id: str


class GlobalEventResponse(GlobalEventBaseModelRequest):
    title: str
    description: str
    date: str
    organizer: str
    venue: str
    tickets: int
    tags: list
    users: list


class GlobalEventRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    date: str
    organizer: str = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    venue: str
    tickets: int
    tags: list
    users: list
