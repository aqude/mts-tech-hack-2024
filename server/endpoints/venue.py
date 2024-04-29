from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session
import services
import uuid
from schemas.venue import VenueResponse, VenueBaseModelResponse, VenueResponseCreate
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
    db: AsyncSession = Depends(get_session),
    title: str = None,
    address: str = None,
    city_id: int = None,
) -> VenueResponseCreate:
    venues = await add_venue_handler(db, title, address, city_id)
    return VenueResponseCreate(
        id=str(venues.id),
        title=str(venues.title),
        address=str(venues.address),
        city_id=int(venues.city_id),
    )


@venue_router.put("/", response_model=VenueResponseCreate)
async def update_venue(
    db: AsyncSession = Depends(get_session),
    venue_id: str = None,
    new_title: str = None,
    new_address: str = None,
    new_city_id: int = None,
) -> VenueResponseCreate | HTTPException:
    try:
        venues = await update_venue_handler(
            db, venue_id, new_title, new_address, new_city_id
        )
        return VenueResponseCreate(
            id=str(venues.id),
            title=str(venues.title),
            address=str(venues.address),
            city_id=int(venues.city_id),
        )
    except ValueError:
        return HTTPException(
            status_code=404, detail="Venue not found with id: {}".format(venue_id)
        )


@venue_router.delete("/", response_model=VenueBaseModelResponse)
async def delete_venue(
    db: AsyncSession = Depends(get_session), venue_id: str = None
) -> VenueBaseModelResponse | HTTPException:
    _venue_id = await delete_venue_handler(db, venue_id)
    if _venue_id is None:
        raise HTTPException(
            status_code=404, detail="Venue not found with id: {}".format(venue_id)
        )

    return VenueBaseModelResponse(id=str(_venue_id))
