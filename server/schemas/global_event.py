from pydantic import BaseModel


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
