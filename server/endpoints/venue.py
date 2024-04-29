from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session
import models
import services
from services.user import get_current_user
import uuid
from schemas.venue import (
    VenueRequest,
    VenueResponse,
    VenueBaseModelResponse,
    VenueResponseCreate,
    VenueUpdateRequest,
)
from services.venue import (
    read_venues_handler,
    add_venue_handler,
    update_venue_handler,
    delete_venue_handler,
)


venue_router = APIRouter(prefix="/api/venue", tags=["Venue"])


@venue_router.get("/", response_model=list[VenueResponse])
async def read_venues(db: AsyncSession = Depends(get_session)) -> list[VenueResponse]:
    venues = await read_venues_handler(db)
    _venues = [
        VenueResponse(
            id=str(venue.id),
            title=str(venue.title),
            address=str(venue.address),
            city_id=int(venue.city_id),
            events=[str(event.id) for event in venue.events],
        )
        for venue in venues
    ]
    return _venues


@venue_router.get("/{venue_id}", response_model=VenueResponse)
async def get_venue(venue_id: uuid.UUID, db: AsyncSession = Depends(get_session)):
    venue = await services.get_venue_by_id(db, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue


@venue_router.post("/", response_model=VenueResponseCreate)
async def add_venue(
    data: VenueRequest,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
) -> VenueResponseCreate:
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    venue = await add_venue_handler(db, data.title, data.address, data.city_id)
    return venue


@venue_router.put("/", response_model=VenueResponseCreate)
async def update_venue(
    data: VenueUpdateRequest,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
) -> VenueResponseCreate | HTTPException:
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    venue = await services.get_venue_by_id(db, data.id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return await update_venue_handler(db, venue, data)


@venue_router.delete("/{venue_id}", response_model=VenueBaseModelResponse)
async def delete_venue(
    venue_id: uuid.UUID,
    db: AsyncSession = Depends(get_session),
    user: models.User = Depends(get_current_user),
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    venue = await services.get_venue_by_id(db, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return await delete_venue_handler(db, venue)
