import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import GlobalEvent


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
    db: AsyncSession,
    title: str,
    description: str,
    date: str,
    organizer_id,
    venue: str,
    tickets: int,
    tags: list,
    users: list,
) -> GlobalEvent:
    uuid_id = str(uuid.uuid4())
    global_event = GlobalEvent(
        id=uuid_id,
        title=title,
        description=description,
        date=date,
        organizer_id=organizer_id,
        venue=venue,
        tickets=tickets,
        tags=tags,
        users=users,
    )
    db.add(global_event)
    await db.commit()
    await db.refresh(global_event)
    return global_event


async def update_global_event_handler(
    db: AsyncSession,
    title: str,
    description: str,
    date: str,
    organizer_id,
    venue: str,
    tickets: int,
    tags: list,
    users: list,
) -> GlobalEvent | None:
    global_event = await db.get(GlobalEvent, title)
    if global_event:
        if title is not None:
            global_event.title = title
        if description is not None:
            global_event.description = description
        if date is not None:
            global_event.date = date
        if organizer_id is not None:
            global_event.organizer_id = organizer_id
        if venue is not None:
            global_event.venue = venue
        if tickets is not None:
            global_event.tickets = tickets
        if tags is not None:
            global_event.tags = tags
        if users is not None:
            global_event.users = users
        await db.commit()
        await db.refresh(global_event)
        return global_event
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
