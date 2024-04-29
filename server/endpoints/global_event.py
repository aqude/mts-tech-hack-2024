import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.global_event import GlobalEventResponse, GlobalEventRequest
from services.global_event import (
    read_global_events_handler,
    add_global_event_handler,
    update_global_event_handler,
    delete_global_event_handler,
)

global_event = APIRouter(prefix="/api/global_event", tags=["GlobalEvent"])


@global_event.get("/", response_model=list[GlobalEventResponse])
async def read_global_events(
    db: AsyncSession = Depends(get_session),
) -> list[GlobalEventResponse]:
    events = await read_global_events_handler(db)
    _events = [
        GlobalEventResponse(
            id=str(event.id),
            title=str(event.title),
            description=str(event.description),
            date=str(event.date),
            organizer=str(event.organizer),
            venue=str(event.venue),
            tickets=int(event.tickets),
            tags=[str(tag.id) for tag in event.tags],
            users=[str(user.id) for user in event.users],
        )
        for event in events
    ]
    return _events


@global_event.post("/", response_model=GlobalEventResponse)
async def add_global_event(
    db: AsyncSession = Depends(get_session), event_data: GlobalEventRequest = None
) -> GlobalEventResponse:
    events = await add_global_event_handler(db, event_data)
    return events


@global_event.put("/", response_model=GlobalEventResponse)
async def update_global_event(
    db: AsyncSession = Depends(get_session),
    title: str = None,
    description: str = None,
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    organizer_id=None,
    venue: str = None,
    tickets: int = None,
    tags: list = None,
    users: list = None,
) -> GlobalEventResponse:
    events = await update_global_event_handler(
        db, title, description, date, organizer_id, venue, tickets, tags, users
    )
    return GlobalEventResponse(
        id=str(events.id),
        title=str(events.title),
        description=str(events.description),
        date=str(events.date),
        organizer=str(events.organizer),
        venue=str(events.venue),
        tickets=int(events.tickets),
        tags=[str(tag.id) for tag in events.tags],
        users=[str(user.id) for user in events.users],
    )


@global_event.delete("/")
async def delete_global_event(
    db: AsyncSession = Depends(get_session), event_id: str = None
) -> str | None:
    _event_id = await delete_global_event_handler(db, event_id)
    if _event_id is None:
        raise HTTPException(
            status_code=404, detail="Event not found with id: {}".format(event_id)
        )
    return _event_id


@global_event.get("/")
async def get_global_event_by_date():
    pass


@global_event.get("/")
async def get_global_event_by_city():
    pass


@global_event.get("/")
async def get_global_event_by_venue():
    pass


@global_event.get("/")
async def get_global_event_by_organizer():
    pass


@global_event.get("/")
async def get_global_event_by_user():
    pass


@global_event.get("/")
async def get_global_event_by_tag():
    pass
