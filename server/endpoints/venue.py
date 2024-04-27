from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session
from schemas.venue import VenueResponse
import services
import uuid


venue_router = APIRouter(prefix="/api/venue", tags=["Venue"])


@venue_router.get("/", response_model=list[VenueResponse])
async def get_venues(db: AsyncSession = Depends(get_session)):
    venues = await services.get_venues(db)
    return venues


@venue_router.get("/{venue_id}", response_model=VenueResponse)
async def get_venue(venue_id: uuid.UUID, db: AsyncSession = Depends(get_session)):
    venue = await services.get_venue_by_id(db, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue
