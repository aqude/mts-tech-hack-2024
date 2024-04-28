import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Venue
from schemas.venue import VenueResponse


# места проведения мероприятий

async def read_venues_handler(db: AsyncSession) -> list[Venue]:
    venues = await db.execute(select(Venue).options(selectinload(Venue.events)))
    return venues.scalars().all()


async def add_venue_handler(db: AsyncSession, title: str, address: str, city_id: int) -> Venue:
    uuid_id = str(uuid.uuid4())  # Генерация UUID
    venue = Venue(id=uuid_id, title=title, address=address, city_id=city_id)
    db.add(venue)
    await db.commit()
    await db.refresh(venue)
    return venue


async def update_venue_handler(db: AsyncSession, venue_id: str, new_title: str = None, new_address: str = None,
                               new_city_id: int = None) -> Venue | None:
    venue = await db.get(Venue, venue_id)
    if venue:
        if new_title is not None:
            venue.title = new_title
        if new_address is not None:
            venue.address = new_address
        if new_city_id is not None:
            venue.city_id = new_city_id
        await db.commit()
        await db.refresh(venue)
        return venue
    else:
        raise ValueError("Venue not found with id: {}".format(venue_id))


async def delete_venue_handler(db: AsyncSession, id: str) -> str | None:
    venue = await db.execute(select(Venue).options(selectinload(Venue.events)).where(Venue.id == id))
    venue = venue.scalar()
    if not venue:
        return None
    await db.delete(venue)
    await db.commit()
    return venue.id
