from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import uuid


async def get_organizers(session: AsyncSession) -> list[models.Organizer]:
    result = await session.execute(
        select(models.Organizer).order_by(models.Organizer.name)
    )
    return list(result.scalars().all())


async def get_organizer_by_id(
    session: AsyncSession, organizer_id: uuid.UUID
) -> models.Organizer | None:
    result = await session.execute(
        select(models.Organizer).where(models.Organizer.id == organizer_id)
    )
    return result.scalar()
