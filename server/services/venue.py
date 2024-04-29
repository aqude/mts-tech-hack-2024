from typing import Sequence
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
import models
from models import Venue
from schemas.venue import VenueResponse, VenueUpdateRequest


async def get_venues(session: AsyncSession) -> list[models.Venue]:
    result = await session.execute(select(models.Venue).order_by(models.Venue.title))
    return list(result.scalars().all())


async def get_venue_by_id(
    session: AsyncSession, venue_id: uuid.UUID
) -> models.Venue | None:
    result = await session.execute(
        select(models.Venue).where(models.Venue.id == venue_id)
    )
    return result.scalar()


# места проведения мероприятий
async def read_venues_handler(db: AsyncSession) -> Sequence[Venue]:
    venues = await db.execute(select(Venue).options(selectinload(Venue.events)))
    return venues.scalars().all()


async def add_venue_handler(
    db: AsyncSession, title: str, address: str, city_id: int
) -> Venue:
    uuid_id = str(uuid.uuid4())  # Генерация UUID
    venue = Venue(id=uuid_id, title=title, address=address, city_id=city_id)
    db.add(venue)
    await db.commit()
    await db.refresh(venue)
    return venue


async def update_venue_handler(
    db: AsyncSession, venue: Venue, data: VenueUpdateRequest
) -> Venue:
    venue.title = data.title
    venue.address = data.address
    venue.city_id = data.city_id
    await db.commit()
    await db.refresh(venue)
    return venue


async def delete_venue_handler(db: AsyncSession, venue: Venue) -> None:
    await db.delete(venue)
    await db.commit()
