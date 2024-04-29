import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import GlobalEvent, Organizer, Venue
from schemas.global_event import GlobalEventRequest, GlobalEventResponse


async def read_global_events_handler(db: AsyncSession) -> list[GlobalEvent]:
    stmt = select(GlobalEvent).options(
        selectinload(GlobalEvent.tags),
        selectinload(GlobalEvent.users),
        selectinload(GlobalEvent.venue),
        selectinload(GlobalEvent.organizer),
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def add_global_event_handler(
    db: AsyncSession, event_data: GlobalEventRequest
) -> GlobalEventResponse:
    organizer = await db.get(Organizer, event_data.organizer)
    venue = await db.get(Venue, event_data.venue)
    global_event = GlobalEvent(
        title=event_data.title,
        description=event_data.description,
        date=event_data.date,
        organizer=organizer,
        venue=venue,
        tickets=event_data.tickets,
        tags=event_data.tags,
        users=event_data.users,
    )
    db.add(global_event)
    await db.commit()
    await db.refresh(global_event)
    return GlobalEventResponse(**global_event.dict())


async def update_global_event_handler(
    db: AsyncSession, event_data: GlobalEventRequest
) -> GlobalEventResponse | None:
    global_event = await db.get(GlobalEvent, event_data.id)
    if global_event:
        if event_data.title is not None:
            global_event.title = event_data.title
        if event_data.description is not None:
            global_event.description = event_data.description
        if event_data.date is not None:
            global_event.date = event_data.date
        if event_data.organizer_id is not None:
            global_event.organizer_id = event_data.organizer_id
        if event_data.venue is not None:
            global_event.venue = event_data.venue
        if event_data.tickets is not None:
            global_event.tickets = event_data.tickets
        if event_data.tags is not None:
            global_event.tags = event_data.tags
        if event_data.users is not None:
            global_event.users = event_data.users
        await db.commit()
        await db.refresh(global_event)

        return GlobalEventResponse(**global_event.dict())
    else:
        return None


async def delete_global_event_handler(db: AsyncSession, id: str) -> str | None:
    global_event = await db.execute(
        select(GlobalEvent)
        .options(selectinload(GlobalEvent.tags), selectinload(GlobalEvent.users))
        .where(GlobalEvent.id == id)
    )
    if not global_event:
        return None
    await db.delete(global_event)
    await db.commit()
    return global_event.id


async def get_global_event_by_date_handler():
    pass


async def get_global_event_by_city_handler():
    pass


async def get_global_event_by_venue_handler():
    pass


async def get_global_event_by_organizer_handler():
    pass


async def get_global_event_by_user_handler():
    pass


async def get_global_event_by_tag_handler():
    pass
