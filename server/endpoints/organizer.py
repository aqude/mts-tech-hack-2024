from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.organizer import OrganizerResponse
from core.database import get_session
import services
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
