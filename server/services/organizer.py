from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import uuid

from schemas.organizer import OrganizerUpdateRequest


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


async def create_organizer(
    session: AsyncSession, name: str, description: str
) -> models.Organizer:
    organizer = models.Organizer(id=uuid.uuid4(), name=name, description=description)
    session.add(organizer)
    await session.commit()
    await session.refresh(organizer)
    return organizer


async def update_organizer(
    session: AsyncSession, organizer: models.Organizer, data: OrganizerUpdateRequest
) -> models.Organizer:
    organizer.name = data.name
    organizer.description = data.description
    await session.commit()
    await session.refresh(organizer)
    return organizer


async def delete_organizer(session: AsyncSession, organizer: models.Organizer):
    await session.delete(organizer)
    await session.commit()
