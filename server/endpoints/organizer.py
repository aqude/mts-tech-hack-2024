from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.organizer import (
    OrganizerResponse,
    OrganizerRequest,
    OrganizerUpdateRequest,
)
from core.database import get_session
import services
import models
from services.user import get_current_user
import uuid


organizer_router = APIRouter(prefix="/api/organizer", tags=["Organizer"])


@organizer_router.get("/", response_model=list[OrganizerResponse])
async def get_organizers(db: AsyncSession = Depends(get_session)):
    organizers = await services.get_organizers(db)
    return organizers


@organizer_router.get("/{organizer_id}", response_model=OrganizerResponse)
async def get_organizer(
    organizer_id: uuid.UUID, db: AsyncSession = Depends(get_session)
):
    organizer = await services.get_organizer_by_id(db, organizer_id)
    if not organizer:
        raise HTTPException(status_code=404, detail="Organizer not found")
    return organizer


# Admin endpoints
@organizer_router.post("/", response_model=OrganizerResponse)
async def add_organizer(
    data: OrganizerRequest,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return await services.create_organizer(db, data.name, data.description)


@organizer_router.put("/", response_model=OrganizerResponse)
async def update_organizer(
    data: OrganizerUpdateRequest,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    organizer = await services.get_organizer_by_id(db, data.id)
    if not organizer:
        raise HTTPException(status_code=404, detail="Organizer not found")

    return await services.update_organizer(db, organizer, data)


@organizer_router.delete("/{organizer_id}")
async def delete_organizer(
    organizer_id: uuid.UUID,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    organizer = await services.get_organizer_by_id(db, organizer_id)
    if not organizer:
        raise HTTPException(status_code=404, detail="Organizer not found")
    await services.delete_organizer(db, organizer)
