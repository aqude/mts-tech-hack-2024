import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models


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
