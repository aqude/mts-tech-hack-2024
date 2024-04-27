from select import select

from models import GlobalEvent


async def read_global_events(session) -> list[GlobalEvent]:
    global_events = await session.execute(select(GlobalEvent))
    return global_events.scalars().all()


async def add_global_event(session, title, description, date, organizer, venue, tickets, tags, users):
    global_event = GlobalEvent(title=title, description=description, date=date, organizer=organizer, venue=venue, tickets=tickets, tags=tags, users=users)
    session.add(global_event)
    await session.commit()
    await session.refresh(global_event)
    return global_event

async def update_global_event():
    pass

async def delete_global_event():
    pass
async def get_global_event_by_date():
    pass

async def get_global_event_by_city():
    pass

async def get_global_event_by_venue():
    pass

async def get_global_event_by_organizer():
    pass

async def get_global_event_by_user():
    pass

async def get_global_event_by_tag():
    pass