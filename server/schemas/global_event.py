import datetime
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


class GlobalEvent(BaseModel):
    title: str
    description: str
    organizer_id: str = uuid.uuid4()
    venue: str = uuid.uuid4()
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tickets: int


class GlobalEventRequest(GlobalEvent):
    id: str
